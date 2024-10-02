from Crypto.Util.number import *
from pwn import *
from math import gcd
from subprocess import run

def query(n):
    io.recvuntil(b"? ")
    io.sendline(str(n).encode())
    return int(io.recvline().strip().decode(), 16)

if args.REMOTE or args.HOST or args.PORT:
    io = remote(args.HOST or "localhost", args.PORT or "5000")
    io.recvline()
    io.sendlineafter(b": ", run(io.recvline().decode(), shell=True, check=True, capture_output=True).stdout.strip())
else:
    io = process(['python3', 'decryption-as-a-service.py'])
line = io.recvline()
print(line)
exec(line)
vals = [query(1<<k) for k in range(1025, 1034)]
vals2 = [vals[k]*vals[k+2]-vals[k+1]**2 for k in range(len(vals)-2)]
N = gcd(*vals2)
for i in range(2, 1000):
    if N % i == 0:
        N //= i 
print(N.bit_length())
f2 = query(pow(1<<1025, -1, N) * encrypted_flag % N)
io.close()
print(long_to_bytes(vals[0] * f2 % N))