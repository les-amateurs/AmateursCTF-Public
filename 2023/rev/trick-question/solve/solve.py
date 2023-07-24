import z3
import hashlib
import random

flag_parts = []
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

flag_parts.append("sn0h7YP"[::-1])

s = z3.Solver()
parts = [z3.BitVec(f"part_{i}", 8) for i in range(3)]
for part in parts:
    s.add(part >= 32)
    s.add(part <= 126)
s.add(parts[0] + parts[1] - parts[2] == 160)
s.add(parts[1] + parts[2] - parts[0] == 68)
s.add(parts[2] + parts[0] - parts[1] == 34)

s.check()
m = s.model()
part = "".join(chr(m[parts[i]].as_long()) for i in range(3))
flag_parts.append(part)

for a in alphabet:
    if hashlib.sha256(a.encode()).hexdigest() == '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a':
        random.seed(a.encode())
        flag_parts.append(a)
        break

order = list(range(6))
part = [49, 89, 102, 109, 108, 52]
tmp = part.copy()
random.shuffle(order)
print(order)
for i in order:
    part[i] = tmp[order.index(i)]
flag_parts.append("".join(chr(i) for i in part))

flag_parts.append("0f")

r = [random.randint(0, 0xFFFFFFFF) for i in range(3)]
n = [0xFBFF4501, 825199122, 0xFEEF2AA6]
part = [(r ^ n).to_bytes(4, 'little') for r, n in zip(r, n)]
part[2] = part[2][:-1]

flag_parts.append(b"".join(part).decode())

c = 0x29ee69af2f3
part = b""
while c:
    part += bytes([c % 128])
    c //= 128

flag_parts.append(part.decode()[::-1])

print("amateursCTF{" + "_".join(flag_parts) + "}")