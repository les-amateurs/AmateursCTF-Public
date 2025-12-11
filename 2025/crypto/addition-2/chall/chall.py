#!/usr/local/bin/python
from Crypto.Util.number import *
from random import getrandbits, choice
import hashlib

flag = open('flag.txt','rb').read().strip()
assert len(flag) == 72
flag = bytes_to_long(flag) << 256

n = getPrime(1024) * getPrime(1024)
e = 3

print(f'{n, e = }')

while True:
    cs = [flag + getrandbits(256) for _ in range(100000)]
    scramble = int(input('scramble the flag: '))

    ms = [(m + scramble)%n for m in cs]

    print('scrambling...')

    c = choice([pow(m, e, n) for m in ms])
    print(f'{c = }')