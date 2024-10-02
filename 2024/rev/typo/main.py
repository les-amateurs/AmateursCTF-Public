import random
random.seed(1684050472)

flag = bytearray(open('flag.txt', 'rb').read())

ar = '\r'r'\r''r''\\r'r'\\r\r'r'r''r''\\r'r'r\r'r'r\\r''r'r'r''r''\\r'r'\\r\r'r'r''r''\\r'r'rr\r''\r''r''r\\'r'\r''\r''r\\\r'r'r\r''\rr'

arr = [
    b'arRRrrRRrRRrRRrRr',
    b'aRrRrrRRrRr',
    b'arRRrrRRrRRrRr',
    b'arRRrRrRRrRr',
    b'arRRrRRrRrrRRrRR'
    b'arRRrrRRrRRRrRRrRr',
    b'arRRrrRRrRRRrRr',
    b'arRRrrRRrRRRrRr'
    b'arRrRrRrRRRrrRrrrR',
]

op1 = lambda x: bytearray([i + 1 for i in x])
op2 = lambda x: bytearray([i - 1 for i in x])
def op3(x):
    for i in range(0, len(x), 2):
        x[i], x[i + 1] = x[i + 1], x[i]
    for i in range(1, len(x) - 1, 2):
        x[i], x[i + 1] = x[i + 1], x[i]
    return x
ops = [op3, op1, op2]
ops = [random.choice(ops) for _ in range(128)]

def func1(arr, ar):
    for r in ar:
        arr = ops[r](arr)
    return arr

flag = func1(flag, ar.encode())
print(flag, flag.hex())

def func2(arr, ar):
    ar = int(ar.hex(), 17)
    for r in arr:
        ar += int(r, 35)
    return bytes.fromhex(hex(ar)[2:])

flag = func2(arr, flag)
print(flag, flag.hex())