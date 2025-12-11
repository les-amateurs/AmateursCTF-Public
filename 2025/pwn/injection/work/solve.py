from pwn import *

p = remote("localhost", 1337)

code = open("solve.elf", "rb").read()
p.sendlineafter(b": ", f"{len(code)}".encode())
p.send(code)

p.interactive()