#!/usr/local/bin/python3

from random import getrandbits
from Crypto.Util.number import *

flag = bytes_to_long(b'sdkfljhaskfljahsdfasdkjfhaskldjfhasdlkfjkljhaskljdfh')
k = flag.bit_length()
m = getPrime(flag.bit_length() + 1)


def lcg(seed = getrandbits(k)):
    c = getrandbits(k//8)
    print(c)
    a = flag
    while True:
        nseed = (a * seed + c) % m
        c = (a * c + seed) % m
        seed = nseed
        yield seed


x = iter(lcg(int(input('seed? '))))
for _ in range(2**16):
    next(x)

q = next(x)
print(f'{m = }')
print(f'{q = }')

# send seed = 0
# l * c0 = q0 (mod m0) = r0 (mod m0 * m1)
# l * c1 = q1 (mod m1) = r1 (mod m0 * m1)
# l * c0 * c1 = (q + m0*h) * c1 = (r + m1*i) * c0

# h,i,c0,c1 -> small
# q 1 0 0
# -r 0 1 0
# m0 0 0 1
# -m1 0 0 1