l = 32 # oops

c = bytes.fromhex(open('../dist/out.txt').read())
c, cflag = c[:-47], c[-47:]

def get_cands(a):
    cands = []
    for i in range(256):
        for j in a:
            if j ^ i in b'\t\n\r \v\f':
                # print(i, j)
                break
            i += 1
            i %= 256
        else:
            cands.append(i)
    return cands

b = {}

for i in range(l):
    b[(i - len(c)) % l] = get_cands(c[i::l])
print(b)

x = []
for i,j in enumerate(cflag):
    x.append(j ^ b[i%32][0] + i//32)
print(b'amateursCTF{' + bytes(x) + b'}')