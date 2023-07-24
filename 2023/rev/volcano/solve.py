from math import lcm
import random
bear_base = 18476
bear_offset = lcm(*[2, 3, 5, 7, 109])

def is_volcano(x: int):
    c = x.bit_count()
    return c > 16 and c < 27

def sum_of_digits(x: int):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

def is_bear(x: int):
    return x % bear_offset == bear_base

v, b = 0, 0
while True:
    v = random.randint(0, 2**48)
    if is_volcano(v):
        s_v = sum_of_digits(v)
        
        l10 = len(str(v))
        print(f"v = {v}, s = {s_v}, l = {l10}")
        b = bear_offset * (10**(l10 - 1) // bear_offset) + bear_base
        print(f"b = {b}, l = {len(str(b))}") 

        s_b = sum_of_digits(b)
        for c in range(10000):
            b += bear_offset * random.randint(1, 10)
            s_b = sum_of_digits(b)
            if s_b == s_v:
                print(f"v = {v}, b = {b}")
                break
        
        if s_b == s_v:
            break

# this is just a bruting challenge if you haven't noticed
m = 3
secret = 0x1337
while True:
    b_r = pow(secret, v, m)
    v_r = pow(secret, b, m)
    if b_r == v_r:
        print(f"m = {m}, b_r = {b_r}, v_r = {v_r}")
        break
    m += 2

