    BITS 64
    
_start:
    mov rax, `/bin/sh`
    push rax
    mov eax, 0x3c
    mov rdi, rsp
    xor esi, esi
    xor edx, edx
    syscall