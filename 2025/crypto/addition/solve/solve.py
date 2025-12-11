from Crypto.Util.number import *
from pwn import *
from tqdm import tqdm

def recv():
    io.recvuntil(b"c = ")
    return int(io.recvline())

# chatgpt generated polynomial funcs because im too lazy to install sage...
# many trees died for my sins

def poly_mod(p, n):
    """Reduce polynomial coefficients mod n."""
    return [a % n for a in p]

def poly_trim(p):
    """Remove leading zeros."""
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def poly_add(a, b, n):
    """(a + b) mod n"""
    m = max(len(a), len(b))
    res = [(0) for _ in range(m)]
    for i in range(m):
        ai = a[i] if i < len(a) else 0
        bi = b[i] if i < len(b) else 0
        res[i] = (ai + bi) % n
    return poly_trim(res)

def poly_sub(a, b, n):
    """(a - b) mod n"""
    m = max(len(a), len(b))
    res = [(0) for _ in range(m)]
    for i in range(m):
        ai = a[i] if i < len(a) else 0
        bi = b[i] if i < len(b) else 0
        res[i] = (ai - bi) % n
    return poly_trim(res)

def poly_mul(a, b, n):
    """(a * b) mod n"""
    res = [0]*(len(a)+len(b)-1)
    for i in range(len(a)):
        for j in range(len(b)):
            res[i+j] = (res[i+j] + a[i]*b[j]) % n
    return poly_trim(res)

def poly_divmod(a, b, n):
    """Return (q, r) such that a = q*b + r mod n."""
    a = a[:]
    b = poly_trim(b[:])
    if b == [0]:
        raise ZeroDivisionError
    q = [0]*(max(0, len(a)-len(b)+1))
    while len(a) >= len(b) and a != [0]:
        # lead term division
        inv = pow(b[-1], -1, n)  # multiplicative inverse mod n
        coef = a[-1] * inv % n
        shift = len(a) - len(b)
        q[shift] = coef
        subtrahend = [0]*shift + [(coef * c) % n for c in b]
        a = poly_sub(a, subtrahend, n)
    return poly_trim(q), poly_trim(a)

def poly_gcd(a, b, n):
    """Euclidean GCD for polynomials mod n."""
    a, b = poly_trim(a), poly_trim(b)
    while b != [0]:
        _, r = poly_divmod(a, b, n)
        a, b = b, r
    return poly_trim(a)

def poly_for_i(i, k, n):
    """Construct (x+i)^3 - k[i] mod n as coeff list."""
    # Expand (x+i)^3 = x^3 + 3ix^2 + 3i^2x + i^3
    return poly_mod([-k[i] + i**3, 3*i*i, 3*i, 1], n)

def gcd_for_indices(k, i, j, n):
    f = poly_for_i(i, k, n)
    g = poly_for_i(j, k, n)
    return poly_gcd(f, g, n)


# io = process(['python3', 'chall.py'])
io = remote('amt.rs', 36879)
io.sendline(b'\n'.join(str(i).encode()for i in range(1000)))
exec(io.recvline(),globals())
k = {}

for i in tqdm(range(1000)):
    k[i] = recv()
    for j in k:
        if i==j:
            break
        if len(c:=gcd_for_indices(k,i,j,n)) > 1:
            x = (pow(c[1],-1,n) * -c[0]) % n
            print(long_to_bytes(x >> 256))
            1/0

