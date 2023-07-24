import random

def rotate(n):
    # rotate left 2
    return ((n << 2) | (n >> 6)) & 0xff

flag = b"amateursCTF{h0pe_y0u_w3r3nt_t00_ru5ty}"
enc = b""
stuff = []
for f in flag:
    r = random.randint(0, 255)
    enc += bytes([rotate(f ^ r)])
    stuff.append(r)

print(list(enc))
print(list(stuff))