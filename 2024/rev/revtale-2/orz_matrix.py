import secrets

to_encode = "amateursCTF{d0_y0u_pr3f3r_butt3rsc0tch_0r_c1nnam0n?}"

print("Encodable length", len(to_encode))

l_a = []
l_b = []

min_val = 999

shift = 0

for c in to_encode:
    num = ord(c)
    min_val = min(min_val, num)
    num -= shift
    a = secrets.randbelow(num)
    b = num ^ a
    if secrets.randbelow(2):
        l_a.append(a)
        l_b.append(b)
    else:
        l_a.append(b)
        l_b.append(a)

print("Decomposition created")
print("MV", min_val)
print(l_a)
print(l_b)
# print every chunk of 13
print("Stage A")
for i in range(0, len(l_a), 13):
    print(l_a[i:i+13])
    
print("Stage B")
for i in range(0, len(l_b), 13):
    print(l_b[i:i+13])