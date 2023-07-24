import zlib

with open('flag.txt', 'rb') as f:
    flag = "0" + bin(int(f.read().hex(), 16))[2:]
with open('flocto.png', 'rb') as f:
    flocto = f.read()
original = flocto[flocto.index(b"IDAT")+4:-12]

bits = zlib.decompress(original).hex()

def hex_to_bin(inp):
    out = ""
    for i in inp:
        out += bin(int(i, 16))[2:].rjust(4, "0")
    return out

bits = hex_to_bin(bits)

interval = len(bits)//len(flag)
print(interval, len(flag))
old_bits = bits
for i in range(len(flag)):
    bits = bits[:i*interval + i] + flag[i] + bits[i*interval + i:]

print(flag)

# do stuff with it ill finish impl later ig
def diff(x, y):
    diff = ""

    if len(y) < len(x):
        x, y = y, x

    count = 0
    countx = 0
    while countx < len(x):
        if x[countx] != y[count]:
            diff += y[count]
            count += 1
        else:
            count += 1
            countx += 1
    diff += y[count:]
    return diff
#print(diff(old_bits, bits))