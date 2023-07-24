# q-warmup

## Author: flocto

**Solves:** 56

**Points:** 466

---

If a bit flips and no one is around to observe it, does it still cause a bug?

This challenge was done on Qiskit version 0.42.1.

---

**Provided Files:**

- [q-warmup.py](./q-warmup.py)

## Solution
The quantum circuit can easily be reimplemented classically since no real quantum mechanics are used.

See [solve.py](solve.py) for both reimplementations.

Then, you can just brute force all characters and create a map of what character results in what value.

```python
def encode_classic(bits):
    ret = [int(bit) for bit in bits]
    for i in range(7, 0, -1):
        ret[i-1] ^= ret[i]
    
    ret = ''.join([str(bit) for bit in ret])
    ret = int(bits, 2) ^ int(ret, 2)
    return ret


import string

enc = b'\xbe\xb6\xbeXF\xa6\\\xa2\x82\x98\x84R\xb4 X\xb0N\xb4\xbaj^f\xd8\xb4X\xa6\xb6j\xd8\xbc \xa6XjX\xb0\xde\xa2j\xd8Xj~HHV' 
enc_map = {encode_classic(bin(i)[2:].zfill(8)): i for i in string.printable.encode()}
print(enc_map)

flag = b''
for i in enc:
    flag += bytes([enc_map[i]])

print(flag)
# amateursCTF{n0thing_qU4ntum_4b0ut_th1s_4t_All}
```