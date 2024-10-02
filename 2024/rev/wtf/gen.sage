p = 1000000007
P = GF(p)

a = int.from_bytes(b'sbg', 'little')
b = int.from_bytes(b'love', 'little')
c = int.from_bytes(b'lcg', 'little')
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
show(M) 

order = M.multiplicative_order()
order = int(order)
print(order, order.bit_length())
key = order.to_bytes((order.bit_length() + 7) // 8, 'big')
print(key, len(key), key.hex())

flag = b'TH3_8357_C0m3_4_th0s3_who_W41t'
print(flag, len(flag))

def xor(a, b):
    return bytes([x ^^ y for x, y in zip(a, b)])

print(xor(flag, key).hex())