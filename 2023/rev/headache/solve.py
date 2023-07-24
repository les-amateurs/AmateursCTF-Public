# hi i suck at using lief so here's a full manual solve
data = open("headache", "rb").read()

start_real = 0x1290
start_virt = 0x401290

conditions = []

i_real = 0x1290
i_virt = start_virt
while True:
    if data[i_real: i_real + 2] == b'\x31\xc0': # only occurs on final level
        i_real += 2; i_virt += 2 

    if data[i_real + 2] == 0x3f: # no offset
        a = data[i_real: i_real + 3]
        a = 0
        i_real += 3; i_virt += 3
    else:
        a = data[i_real: i_real + 4]
        a = a[-1]
        i_real += 4; i_virt += 4

    if data[i_real + 2] == 0x3f: # no offset
        b = data[i_real: i_real + 3]
        b = 0
        i_real += 3; i_virt += 3
    else:
        b = data[i_real: i_real + 4]
        b = b[-1]
        i_real += 4; i_virt += 4

    cmp = data[i_real: i_real + 4]
    i_real += 4; i_virt += 4
    cmp = cmp[-1]
    conditions.append((a, b, cmp))

    if data[i_real] == 0x74: # jz short
        jz = data[i_real: i_real + 2]
        jz_offset = jz[1]
        i_real += 2; i_virt += 2
    else: # jz near
        jz = data[i_real: i_real + 6]
        jz_offset = int.from_bytes(jz[2:], "little", signed=True)
        i_real += 6; i_virt += 6

    i_real += jz_offset; i_virt += jz_offset
    # print(hex(i_real), hex(i_virt))

    xor = data[i_real: i_real + 5]
    xor = int.from_bytes(xor[1:], "little")
    # print(hex(xor))
    i_real += 5; i_virt += 5

    lea = data[i_real: i_real + 8]
    # print(lea)
    lea = int.from_bytes(lea[4:], "little", signed=True)
    # print(hex(lea))
    if lea <= 0:
        break

    lea_offset = lea - start_virt
    # print(hex(lea_offset))

    i_real = start_real + lea_offset; i_virt = start_virt + lea_offset
    print(hex(i_real), hex(i_virt))

    decoded = b""
    i = i_real
    while True:
        nxt = int.from_bytes(data[i: i + 4], "little")
        if nxt == 0:
            break
        nxt ^= xor
        decoded += nxt.to_bytes(4, "little")
        i += 4

    data = data[:i_real] + decoded + data[i_real + len(decoded):]

with open("headache_decoded", "wb") as f:
    f.write(data)

import z3
s = z3.Solver()

length = 0x3d
flag = [z3.BitVec(f"flag_{i}", 8) for i in range(length)]

for a, b, c in conditions:
    s.add(flag[a] ^ flag[b] == c)

s.add(flag[0] == b'a'[0])

if s.check() == z3.sat:
    m = s.model()
    flag = "".join([chr(m[f].as_long()) for f in flag])
    print(flag)