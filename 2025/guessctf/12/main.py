#!/usr/local/bin/python
import random
m = 128
b = 128
while m == 128 or b == 128:  # reduce rng lmao
    m = random.randint(1, 255)
    b = random.randint(100, 156)  # increase variation


flag = "amateursCTF{aN_1t3r!7avE_fi/7iTe_f1n3-FlN3_c1ph3r}".encode()


enc = ""
for i in flag:
    hexs = hex(((i ^ m) + b) % 256)[2:]
    enc += "0" * (2-len(hexs)) + hexs
    m += b
    m = m % 256
print("Flag:", enc)


enc = ""
for i in flag:
    hexs = hex((i * m + b) % 256)[2:]
    enc += "0" * (2-len(hexs)) + hexs
    m += b
    m = m % 256
print("Flag:", enc)


while True:
    print("Type exit to exit.")
    a = input("Encrypt? ").encode()

    if a == b"exit":
        exit(0)

    enc = ""
    if random.randint(0, 1) == 0:
        for i in a:
            hexs = hex(((i ^ m) + b) % 256)[2:]
            enc += "0" * (2-len(hexs)) + hexs
            m += b
            m = m % 256

    else:
        for i in a:
            hexs = hex((i * m + b) % 256)[2:]
            enc += "0" * (2-len(hexs)) + hexs
            m += b
            m = m % 256

    print(enc)