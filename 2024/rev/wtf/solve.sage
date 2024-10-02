enc = b"\xc4\xac\x23\x18\x33\x33\x13\x3c\x9f\xfa\xda\xf4\xd1\x99\x17\x0b\x81\xaa\xea\x27\x9d\x4a\x45\x06\x79\xb9\xf1\x3b\x17\xb4"
p = 0x3b9aca07
P = GF(p)

a = 0x676273
b = 0x65766f6c
c = 0x67636c
seed = 0xf10c70 
print(a, b, c, seed)

N = 12
m = []
for i in range(N):
    row = []
    for j in range(N):
        seed = (a * seed * seed + b * seed + c) % p
        row.append(P(seed))
    m.append(row)

M = Matrix(m)

order = M.multiplicative_order()
order = int(order)
print(order, order.bit_length())
key = order.to_bytes((order.bit_length() + 7) // 8, 'big')
print(key, len(key))

flag = b''

for i in range(len(enc)):
    flag += bytes([enc[i] ^^ key[i % len(key)]])

print(flag)