from Crypto.Util.number import *
import secrets
from math import ceil
from os import urandom
import sys
from tqdm import tqdm

sys.set_int_max_str_digits(10000)
pmax = 512
p = getPrime(128)
ub = [(2**pmax - 1)]
for i in range(16):
    ub.append(ub[-1]//p)
ubits = [i.bit_length() for i in ub]
def get(n, even = False):
    n += 1
    while True:
        x = secrets.randbits(ubits[n])
        if x <= ub[n]:
            if even and x % 2 == 0:
                break
            elif (not even) and x % 2 == 1:
                break
    c = x*p**n
    assert c.bit_length() <= pmax
    return c
def randbelow(n):
    x = secrets.randbits(pmax)
    while x > n:
        x = secrets.randbits(pmax)
    return x
flag = [i for i in b"amateursCTF{3xponents_4re_cool_or_s0mething?!?_4d767c85f66f530c}"]
out = [[] for i in flag]
choice = [i for i in range(9999)]

indices = [[secrets.choice(choice) for i in range(j)] for j in flag]
[indices[i].sort(reverse=True) for i in range(len(flag))]

for i in tqdm(range(len(flag))):
    j = 0
    while indices[i]:
        exp = 0
        while indices[i] and indices[i][-1] == j:
            indices[i].pop()
            exp += 1
        target = get(exp)
        a = randbelow(target)
        b = target - a
        out[i].append((hex(a),hex(b)))
        j += 1
    even = False
    while j < 9999:
        if even and bytes_to_long(urandom(2)) % 100 == 0:
            target = get(1, True)
        else:
            target = get(0, secrets.randbelow(even + 1))
        a = randbelow(target)
        b = target - a
        out[i].append((hex(a),hex(b)))
        j += 1
        even = True
    out[i].append(hex(get(-1, secrets.randbelow(even + 1))))
with open('../out.txt', 'w') as f:
    f.write(str(p) + "\n" + str(out))
