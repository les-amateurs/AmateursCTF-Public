import random

seed = 1684050472
random.seed(seed)
op1 = lambda x: bytearray([i + 1 for i in x])
op2 = lambda x: bytearray([i - 1 for i in x])
def op3(x):
    for i in range(0, len(x) - 1, 2):
        x[i], x[i + 1] = x[i + 1], x[i]
    for i in range(1, len(x) - 1, 2):
        x[i], x[i + 1] = x[i + 1], x[i]
    return x
ops = [op3, op1, op2]
ops = [random.choice(ops) for _ in range(128)]

def inv_op3(x):
    for i in range(1, len(x) - 1, 2):
        x[i], x[i + 1] = x[i + 1], x[i]
    for i in range(0, len(x) - 1, 2):
        x[i], x[i + 1] = x[i + 1], x[i]
    return x

assert inv_op3(op3(bytearray(b'hello'))) == b'hello'

inv_ops = [inv_op3, op2, op1]
random.seed(seed)
inv_ops = [random.choice(inv_ops) for _ in range(128)]

def to_base(n, base):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    return alphabet[n] if n < base else to_base(n // base, base) + alphabet[n % base]

enc = '5915f8ba06db0a50aa2f3eee4baef82e70be1a9ac80cb59e5b9cb15a15a7f7246604a5e456ad5324167411480f893f97e3'
enc = bytes.fromhex(enc)

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

def inv_func2(arr, ar):
    ar = int(ar.hex(), 16)
    for r in arr:
        ar -= int(r, 35)
    return bytes.fromhex(to_base(ar, 17))

enc = inv_func2(arr, enc)

def inv_func1(arr, ar):
    for r in reversed(ar):
        arr = inv_ops[r](arr)
    return arr

ar = '\r'r'\r''r''\\r'r'\\r\r'r'r''r''\\r'r'r\r'r'r\\r''r'r'r''r''\\r'r'\\r\r'r'r''r''\\r'r'rr\r''\r''r''r\\'r'\r''\r''r\\\r'r'r\r''\rr'
dec = inv_func1(enc, ar.encode())

print(dec.decode())
