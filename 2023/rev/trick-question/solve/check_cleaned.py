# pycdc check.pyc -c -v 3.10 -o check.py
# Source Generated with Decompyle++
# File: check.pyc (Python 3.10)

# cleaned up copy
import hashlib
import random


def check(input):
    if input[:12] != 'amateursCTF{':
        return False
    if input[-1] != '}':
        return False
    input = input[12:-1]
    if len(input) != 42:
        return False
    
    underscores = None
    for i, x in enumerate(input):
        if x == '_':
            underscores.append(i)
    if underscores != [
            7,
            11,
            13,
            20,
            23,
            35]:
        return False

    input = input.encode().split(b'_')
    if input[0][::-1] != b'sn0h7YP':
        return False
    if (input[1][0] + input[1][1] - input[1][2], input[1][1] + input[1][2] - input[1][0], input[1][2] + input[1][0] - input[1][1]) != (160, 68, 34):
        return False
    if hashlib.sha256(input[2]).hexdigest() != '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a':
        return False

    random.seed(input[2])
    input[3] = list(input[3])
    random.shuffle(input[3])
    if input[3] != [
            49,
            89,
            102,
            109,
            108,
            52]:
        return False
    if input[4] + b'freebie' != b'0ffreebie':
        return False
    
    if int.from_bytes(input[5][0:4], 'little') ^ random.randint(0, 0xFFFFFFFF) != 0xFBFF4501:
        return False
    if int.from_bytes(input[5][4:8], 'little') ^ random.randint(0, 0xFFFFFFFF) != 825199122:
        return False
    if int.from_bytes(input[5][8:12] + b'\x00', 'little') ^ random.randint(0, 0xFFFFFFFF) != 0xFEEF2AA6:
        return False
    
    c = 0
    for i in input[6]:
        c *= 128
        c += i

    if hex(c) != '0x29ee69af2f3':
        return False
    return True
