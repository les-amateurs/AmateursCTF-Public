#define _GNU_SOURCE
#include <err.h>
#include <errno.h>
#include <linux/seccomp.h>
#include <sched.h>
#include <seccomp.h>
#include <stdio.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/random.h>
#include <unistd.h>

#define FD_LOG_STYLE 0
#define FD_IO_STYLE 0
#define FD_ENV_STYLE 0

#include "firedancer/src/flamenco/vm/fd_vm_context.c"
#include "firedancer/src/flamenco/vm/fd_vm_interp.c"
#include "firedancer/src/flamenco/vm/fd_vm_log_collector.c"
#include "firedancer/src/flamenco/vm/fd_vm_stack.c"
#include "firedancer/src/flamenco/vm/fd_vm_syscalls.c"
#include "firedancer/src/flamenco/vm/fd_vm_trace.c"
#include "firedancer/src/util/cstr/fd_cstr.c"
#include "firedancer/src/util/fd_util.c"
#include "firedancer/src/util/log/fd_log.c"
#include "firedancer/src/util/pod/fd_pod.c"

#include "firedancer/src/ballet/base58/fd_base58.c"
#include "firedancer/src/ballet/base64/fd_base64.c"
#include "firedancer/src/ballet/blake3/blake3_portable.c"
#include "firedancer/src/ballet/blake3/fd_blake3.c"
#include "firedancer/src/ballet/keccak256/fd_keccak256.c"
#include "firedancer/src/ballet/murmur3/fd_murmur3.c"
#include "firedancer/src/ballet/sha256/fd_sha256.c"

#include "firedancer/src/util/env/fd_env.c"
#include "firedancer/src/util/io/fd_io.c"
#include "firedancer/src/util/math/fd_stat.c"
#include "firedancer/src/util/scratch/fd_scratch.c"
#include "firedancer/src/util/shmem/fd_shmem_admin.c"
#include "firedancer/src/util/tile/fd_tile.c"
#include "firedancer/src/util/tile/fd_tile_nothreads.cxx"

void setup_seccomp() {
    scmp_filter_ctx ctx;
    ctx = seccomp_init(SCMP_ACT_KILL);
    int ret = 0;
    ret |= seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 0);
    ret |= seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit), 0);
    ret |= seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit_group), 0);
    ret |= seccomp_load(ctx);
    if (ret) {
        errx(1, "seccomp failed");
    }
}

#define PC_MAX 0x8000

void *isolate(ulong n) {
    ulong addr;
    if (sizeof(addr) != getrandom(&addr, sizeof(addr), 0)) {
        errx(1, "failed to retrieve random address");
    }

    addr &= 0x00000FFFFFFFF000;
    n = (n + 0x1000) & ~0xFFF;

    ulong size = n + 0x2000;

    void *obj = mmap((void *)addr, size, PROT_NONE,
                     MAP_ANON | MAP_PRIVATE | MAP_FIXED, -1, 0x1000);
    if (obj == MAP_FAILED) {
        errx(1, "failed to mmap object");
    }

    if (0 > mprotect(obj, n, PROT_READ | PROT_WRITE)) {
        errx(1, "failed to set obj permissions");
    }

    return obj;
}

void challenge(const fd_sbpf_instr_t *instrs, ulong instr_cnt,
               ulong readonly_sz) {
    fd_sbpf_syscalls_t *syscalls =
        fd_sbpf_syscalls_new(isolate(fd_sbpf_syscalls_footprint()));
    fd_vm_register_syscall(syscalls, "abort", fd_vm_syscall_abort);
    fd_vm_register_syscall(syscalls, "sol_panic_", fd_vm_syscall_sol_panic);

    fd_vm_register_syscall(syscalls, "sol_log_", fd_vm_syscall_sol_log);
    fd_vm_register_syscall(syscalls, "sol_log_compute_units_",
                           fd_vm_syscall_sol_log_compute_units);

    fd_vm_register_syscall(syscalls, "sol_sha256", fd_vm_syscall_sol_sha256);
    fd_vm_register_syscall(syscalls, "sol_keccak256",
                           fd_vm_syscall_sol_keccak256);

    fd_vm_register_syscall(syscalls, "sol_alloc_free_",
                           fd_vm_syscall_sol_alloc_free);
    fd_vm_register_syscall(syscalls, "sol_set_return_data",
                           fd_vm_syscall_sol_set_return_data);
    fd_vm_register_syscall(syscalls, "sol_get_return_data",
                           fd_vm_syscall_sol_get_return_data);
    fd_vm_register_syscall(syscalls, "sol_get_stack_height",
                           fd_vm_syscall_sol_get_stack_height);

    fd_vm_register_syscall(syscalls, "sol_get_clock_sysvar",
                           fd_vm_syscall_sol_get_clock_sysvar);
    fd_vm_register_syscall(syscalls, "sol_get_epoch_schedule_sysvar",
                           fd_vm_syscall_sol_get_epoch_schedule_sysvar);
    fd_vm_register_syscall(syscalls, "sol_get_rent_sysvar",
                           fd_vm_syscall_sol_get_rent_sysvar);

    fd_vm_register_syscall(syscalls, "sol_create_program_address",
                           fd_vm_syscall_sol_create_program_address);
    fd_vm_register_syscall(syscalls, "sol_try_find_program_address",
                           fd_vm_syscall_sol_try_find_program_address);
    fd_vm_register_syscall(syscalls, "sol_get_processed_sibling_instruction",
                           fd_vm_syscall_sol_get_processed_sibling_instruction);

    fd_sbpf_calldests_t *local_call_map =
        (fd_sbpf_calldests_t *)fd_sbpf_calldests_new(
            isolate(fd_sbpf_calldests_footprint(PC_MAX)), PC_MAX);

    fd_vm_exec_context_t *ctx = isolate(sizeof(fd_vm_exec_context_t));
    ctx->instrs = instrs;
    ctx->instrs_sz = instr_cnt;
    ctx->heap_sz = 0x1337;
    ctx->compute_meter = 0xffffffffffffffff;
    ctx->syscall_map = syscalls;
    ctx->input = NULL;
    ctx->input_sz = 0;
    ctx->read_only = instrs;
    ctx->read_only_sz = readonly_sz;
    ctx->previous_instruction_meter = 0xffffffffffffffff;

    int fd = open("flag.txt", O_RDONLY);
    read(fd, ctx->heap + 0x1337, 128);
    close(fd);

    ulong validation = fd_vm_context_validate(ctx);
    if (FD_VM_SBPF_VALIDATE_SUCCESS == validation) {
        setup_seccomp();
        ulong status = fd_vm_interp_instrs(ctx);
        printf("done: %ld\n", status);
    } else {
        printf("error: %ld\n", validation);
        errx(1, "invalid program");
    }
}

void challenge_wrapper() {
    ulong program_size;
    printf("program size: ");
    scanf("%ld", &program_size);
    getchar();

    if (program_size > 0x8000) {
        errx(1, "program too big");
    }

    fd_sbpf_instr_t *instrs = isolate(program_size);
    printf("program: ");
    fread((void *)instrs, 1, program_size, stdin);

    ulong instr_cnt;
    printf("instruction count: ");
    scanf("%ld", &instr_cnt);
    getchar();

    if (instr_cnt >= program_size / sizeof(fd_sbpf_instr_t) - 1) {
        errx(1, "invalid instruction count");
    }

    challenge(instrs, instr_cnt, program_size);
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);

    challenge_wrapper();
}