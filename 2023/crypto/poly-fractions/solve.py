from pwn import remote, process
from collections import Counter

r = remote('amt.rs', 31312)
A = 71
B = 73
A_nums = []
B_nums = []

for i in range(10):
    r.recvuntil(b'x: ')
    r.sendline(str(A).encode())
    line = r.recvline().decode().strip()
    num, denom = line.split('/')
    A_nums.append(int(num))
    
for i in range(10):
    r.recvuntil(b'x: ')
    r.sendline(str(B).encode())
    line = r.recvline().decode().strip()
    num, denom = line.split('/')
    B_nums.append(int(num))

msg = ''
while True:
    tnums = [n % A for n in A_nums]
    at_top = Counter(tnums).most_common(1)[0][0]
    A_poss = [at_top, A - at_top, at_top + A, A - at_top + A]

    tnums = [n % B for n in B_nums]
    bt_top = Counter(tnums).most_common(1)[0][0]
    B_poss = [bt_top, B - bt_top, bt_top + B, B - bt_top + B]

    # print(A_poss, B_poss)

    poss = [A_poss[i] for i in range(4) if A_poss[i] == B_poss[i]]
    if len(poss) != 1:
        print('Error')
        break
    
    t = poss[0]
    msg = chr(t) + msg
    print(msg)

    if len(msg) > 50:
        break

    
    CARRY = [0, -1, 1, -2]
    Ac = CARRY[A_poss.index(t)]
    Bc = CARRY[B_poss.index(t)]
    A_nums = [(n - at_top) // A - Ac for n in A_nums if n % A == at_top]
    B_nums = [(n - bt_top) // B - Bc for n in B_nums if n % B == bt_top]
