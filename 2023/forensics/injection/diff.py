def diff(x, y):
    diff = ""

    if len(y) < len(x):
        x, y = y, x

    count = 0
    countx = 0
    zzz = len(x)
    while countx < zzz:
        if x[countx] != y[count]:
            diff += y[count]
        # print(count, countx, count - countx)
        # print(y[count], flag[len(diff)-1])
        # print(y[count-10:count+10])
        # print(x[countx-10:countx+10])
        else:
            countx += 1
        count += 1
    diff += y[count:]
    return diff

with open('flocto.png', 'rb') as f:
    original = f.read()[:-12]
with open('modified.png', 'rb') as f:
    modified = f.read()[:-12]

original = original[original.index(b"IDAT")+4:]
modified = modified[modified.index(b"IDAT")+4:]
def hex_to_bin(inp):
    out = ""
    for i in inp:
        out += bin(int(i, 16))[2:].rjust(4, "0")
    return out
import zlib
original = hex_to_bin(zlib.decompress(original).hex())
modified = hex_to_bin(zlib.decompress(modified).hex())
print(original[:100])
print(modified[:100])
# with open('og.txt', 'w') as f:
#     f.write(original)
# with open('mf.txt', 'w') as f:
#     f.write(modified)
extracted = bytes.fromhex(hex(int(diff(original, modified), 2))[2:])

extracted = [i for i in extracted]

for i in range(len(extracted)):
    if extracted[i] > 127:
        extracted[i] -= 64

extracted = "".join([chr(i) for i in extracted])
    
    

print(extracted)

backwards = bytes.fromhex(hex(int(diff(original[::-1], modified[::-1])[::-1], 2))[2:])

backwards = [i for i in backwards]

for i in range(len(backwards)):
    if backwards[i] > 127:
        backwards[i] -= 128
        backwards[i-1] += 1

backwards = "".join([chr(i) for i in backwards])

print(backwards)



"""

------------------------------------------------------------

Everything below extrapolates from data to recover the flag.

------------------------------------------------------------

"""

gap = len(original) // (456)
#gap -= 1
flag = ""
for i in range(456):
    flag += modified[gap * i + i]
from Crypto.Util.number import *
l2b = b"\x00\x00" + long_to_bytes(int(flag, 2))
y = l2b[27:]
out = ""
for i in l2b:
    if i < 30:
        out += " "
    else:
        out += chr(i)
print(out)

gap = len(original) // (456)
gap -= 1
flag = ""
for i in range(456):
    flag += modified[gap * i + i]
l2b2 = long_to_bytes(int(flag, 2))
out = ""
for i in l2b2:
    if i < 30:
        out += " "
    else:
        out += chr(i)
print(out)
z = l2b2[:27]

print((z+y).decode())

