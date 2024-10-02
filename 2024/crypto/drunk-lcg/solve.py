from Crypto.Util.number import *
from pwn import *
context.log_level = 'error'
m = 150094635296999121

def randbelow(n, k):
    a = k
    while a < n:
        a *= m
        a += k
    return a % n
def unhex(n):
    return int(n, 16)
values = []
for i in range(100): # turn up the amount if you want it to work more often.
    io = process(['python3', 'drunk-lcg.py'])
    io.recvline()
    values.append(io.recvline().strip().decode())
    io.close()

bitlen = len(values[0]) * 4
bm = 1<<bitlen
large = randbelow(bm, 1)
small = randbelow(bm, m-2)*pow((m-2), -1, bm) % bm
values = [i for i in map(unhex, values)]
bytelen = bitlen//8
header = bytes_to_long(b"amateursCTF{" + b"\0" * (bytelen - len(b"amateursCTF{")))
print("org =",values)
print("xor =",header)
print("values =",[i ^ header for i in values])
print("bm =",bm)
print("bitlen =",bitlen)
print(f"small, large = {small}, {large}")