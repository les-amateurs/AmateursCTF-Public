from random import randint, choice
from base64 import b64encode

flag = "amateursCTF{i_h4v3_a_spli77ing_headache_1_r3qu1re_m04r_sl33p}"
length = len(flag)
chrs = set(range(length))

seen_xors = set()

shellcode = b""

while chrs:
    while (a := randint(0, length-1)) == (b := randint(0, length-1)):
        pass
    if a in chrs: chrs.remove(a)
    if b in chrs: chrs.remove(b)

    check = \
f"""
    mov r15b, byte [rdi + {a}]
    xor r15b, byte [rdi + {b}]
    cmp r15b, {ord(flag[a]) ^ ord(flag[b])}
"""

    if not shellcode:
        shellcode = \
f"""
    xor eax, eax
    {check}
    sete al
    ret
"""
    else:
        x = randint(0, (1 << 32) - 1)
        while x in seen_xors:
            x = randint(0, (1 << 32) - 1)
        seen_xors.add(x)
        shellcode = \
f"""
    {check}
    je decode_{x}
    xor eax, eax
    ret

    align 4
encoded_{x}:
    {shellcode}
    align 4
encoded_{x}_end:
    dd 0

decode_{x}:
    mov eax, {x}
    lea rsi, encoded_{x}
.loop:
    xor dword [rsi], eax
    add rsi, 4
    cmp dword [rsi - 4], eax
    jne .loop
    call encoded_{x}
    ret
"""

shellcode = \
f"""
    global headache
    section .text

headache:
    {shellcode}

    align 4
"""

with open("firstpass.asm", "w+") as f:
    f.write(shellcode)