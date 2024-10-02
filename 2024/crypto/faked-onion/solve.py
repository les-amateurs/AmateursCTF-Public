from pwn import *
from Crypto.Util.strxor import strxor

io = process(['python3', 'faked-onion.py'], level='error')

thing = b"\x00"*15
keys = {}
for i in range(256):
    io.sendline(b"1")
    io.recvuntil(b": ")
    io.sendline((thing+chr(i).encode()).hex().encode())
    keys[i] = bytes.fromhex(io.recvline().strip().decode())[1:]

io.sendline(b"2")
io.recvuntil(b"> ")
flag = bytes.fromhex(io.recvline().strip().decode())
fleg = b""
for i in range(len(flag)//16+1):
    a = strxor(keys[flag[i*16]][:len(flag[i*16+1:i*16+16])], flag[i*16+1:i*16+16])
    fleg += a
    fleg += chr(flag[i*16]).encode()
print(fleg)