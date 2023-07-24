import random

fill = b'sorry_this_isnt_the_flag_this_time.'
flag = b'amateursCTF{d0n3_4nd_deRust3d}'

enc = []
stuff = []
item = []

def rotate(n):
    # rotate left 2
    return ((n << 2) | (n >> 6)) & 0xff

for i in range(len(fill)):
    r = random.randint(0, 255)
    if i < len(flag):
        item.append(fill[i] ^ flag[i] ^ r)
    
    enc.append(rotate(fill[i] ^ r))
    stuff.append(r)

print(enc)
print(stuff)
print(item, len(item))