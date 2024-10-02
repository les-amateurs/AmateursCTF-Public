#define _GNU_SOURCE
#include "color.h"
#include <asm/prctl.h>
#include <err.h>
#include <fcntl.h>
#include <linux/seccomp.h>
#include <seccomp.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/syscall.h>
#include <time.h>
#include <unistd.h>

typedef uint64_t u64;
typedef uint32_t u32;
typedef uint16_t u16;
#define BYTES ((uint64_t)0x1000)

__attribute__((naked)) void _munmap(void *addr, size_t len) {
    asm volatile("push r10\n"
                 "push r9\n"
                 "push r8\n"

                 "mov eax, 11\n"
                 "mov r10, rcx\n"
                 "syscall\n"

                 "pop r8\n"
                 "pop r9\n"
                 "pop r10\n"
                 "ret\n"
                 :
                 :
                 : "memory");
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    char *code = mmap((void *)0x1337000, BYTES, PROT_READ | PROT_WRITE,
                      MAP_ANON | MAP_PRIVATE | MAP_FIXED_NOREPLACE, -1, 0);
    if (code == MAP_FAILED) {
        errx(1, red("mmap failed"));
    }

    printf(white("> "));
    fread(code, 1, BYTES, stdin);

    for (int i = 0; i < BYTES - 1; i++) {
        u16 word = *(u16 *)(code + i);
        if (word == 0x050F || word == 0x80CD) {
            errx(1, red("invalid instruction!"));
        }
    }

    if (0 > mprotect(code, BYTES, PROT_READ | PROT_EXEC)) {
        errx(1, red("mprotect failed"));
    }

    if (0 > syscall(SYS_arch_prctl, ARCH_SET_FS, 0)) {
        errx(1, red("failed to set fsbase"));
    }

    if (0 > syscall(SYS_arch_prctl, ARCH_SET_GS, 0)) {
        errx(1, red("failed to set gsbase"));
    }

    asm volatile("mov rax, %[code]\n"
                 "mov rcx, 0x1337133713371337\n"
                 "mov rdx, rcx\n"
                 "mov rbx, rcx\n"
                 "mov rdi, rcx\n"
                 "mov rsi, rcx\n"
                 "mov rbp, rcx\n"
                 "mov rsp, rcx\n"
                 "mov r8,  rcx\n"
                 "mov r9,  rcx\n"
                 "mov r10, rcx\n"
                 "mov r11, rcx\n"
                 "mov r12, rcx\n"
                 "mov r13, rcx\n"
                 "mov r14, rcx\n"
                 "mov r15, rcx\n"
                 "jmp rax\n"
                 :
                 : [code] "code"(code)
                 : "memory");
}