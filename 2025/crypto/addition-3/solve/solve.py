from pwn import *
from math import isqrt
from Crypto.Util.number import *
from tqdm import tqdm

def query(k):
    exec(io.recvline(),globals())
    io.recvuntil(b"scramble the flag: ")
    io.sendline(str(isqrt(n) - k))
    # io.recvline()
    x = time.time()
    io.recvline()
    io.recvline()
    return time.time() - x

# io = process(['python3', 'chall.py'])
io = remote('amt.rs', 40143)

p = b'amateursCTF{'
bits = ''
fl = 52
l = 512

q = len(p)*8 + len(bits)

bit = 2**(fl*8-q+l)
known = bytes_to_long(p + bytes([int(bits.ljust(8,'1'),2)]) + b'\xff' * (fl + l//8 - 1 - q//8))

v = lambda k:min([query(k) for _ in range(5)])

bases = [v(known)]


for i in tqdm(range(fl*8-q)):
    if sum(bases)/len(bases)*0.95 <= (s:=v(known - bit)):
        known -= bit
        bases.append(s)
    bit >>= 1
    print(bases, s)
    print(long_to_bytes(known >> l))