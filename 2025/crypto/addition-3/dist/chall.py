#!/usr/local/bin/python
from Crypto.Util.number import *
import os
from random import getrandbits, choice
import hashlib

flag = open('flag.txt','rb').read().strip()
assert len(flag) == 52
flag = bytes_to_long(flag) << 512

while True:
    n = int(os.popen('openssl genrsa 2048 | openssl rsa -noout -modulus').read()[8:], 16)
    e = 3

    print(f'{n, e = }')
    cs = [flag + getrandbits(512) for _ in range(100000)]
    scramble = int(input('scramble the flag: '))

    ms = [(m + scramble)%n for m in cs]

    print('scrambling...')

    c = choice([pow(m, e, n) for m in ms])
    print(f'{c = }')