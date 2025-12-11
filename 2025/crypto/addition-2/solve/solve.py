from pwn import *
from math import isqrt
from Crypto.Util.number import *
from tqdm import tqdm

def query(k):
    io.recvuntil(b"scramble the flag: ")
    io.sendline(str(k))
    # io.recvline()
    x = time.time()
    io.recvline()
    io.recvline()
    return time.time() - x

# io = process(['python3', 'chall.py'])
io = remote('amt.rs', 43801)
exec(io.recvline(),globals())

p = b'amateursCTF{n0_th3_fl4g_1s_n0T_th3_Same_1f_y0'

bit = 2**(72*8-len(p)*8+256)
known = isqrt(n) - bytes_to_long(p + b'\xff' * (104 - len(p)))

v = lambda k:sum([query(k) for _ in range(1)])/1

bases = [v(known)]


for i in tqdm(range(72*8-len(p)*8)):
    if (k:=sum(bases)/len(bases)*0.9 <= (s:=v(known + bit))):
        known += bit
        bases.append(s)
    bit >>= 1
    print(bases, s)
    print(long_to_bytes(isqrt(n) - known >> 256))