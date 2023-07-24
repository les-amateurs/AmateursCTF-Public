from ctypes import *
# https://stackoverflow.com/questions/2588364/python-tea-implementation
def encipher(v, k):
    y = c_uint32(v[0])
    z = c_uint32(v[1])
    sum = c_uint32(0)
    delta = 0x9e3779b9
    n = 32
    w = [0,0]

    while(n>0):
        sum.value += delta
        y.value += ( z.value << 4 ) + k[0] ^ z.value + sum.value ^ ( z.value >> 5 ) + k[1]
        z.value += ( y.value << 4 ) + k[2] ^ y.value + sum.value ^ ( y.value >> 5 ) + k[3]
        n -= 1

    w[0] = y.value
    w[1] = z.value
    return w

def decipher(v, k):
    y = c_uint32(v[0])
    z = c_uint32(v[1])
    sum = c_uint32(0xc6ef3720)
    delta = 0x9e3779b9
    n = 32
    w = [0,0]

    while(n>0):
        z.value -= (( y.value << 4 ) + k[2]) ^ (y.value + sum.value) ^ (( y.value >> 5 ) + k[3])
        y.value -= (( z.value << 4 ) + k[0]) ^ (z.value + sum.value) ^ (( z.value >> 5 ) + k[1])
        sum.value -= delta
        n -= 1

    w[0] = y.value
    w[1] = z.value
    return w

from Crypto.Util.number import bytes_to_long, long_to_bytes

key = [69420, 1412141, 1936419188, 1953260915]

enc = open("data.txt", "r").read().strip().splitlines() # exfil data from scratch project
enc = [int(i) for i in enc]
enc = bytes(enc)
print(enc)
msg = b''
for i in range(0, len(enc), 8):
    block = enc[i:i+8]
    v = [bytes_to_long(block[:4]), bytes_to_long(block[4:])]
    block = decipher(v, key)
    msg += long_to_bytes(block[0]) + long_to_bytes(block[1])
print(msg)


