# trick question

## Author: flocto

**Solves:** 62

**Points:** 462

---

Which one do you hate more: decompiling pycs or reading Python bytecode disassembly?
Just kidding that's a trick question.

Run with Python version `3.10`.

Flag is `amateursCTF{[a-zA-Z0-9_]+}`

---

**Provided Files:**

- [trick-question.pyc](./trick-question.pyc)

## Solution
See [solve folder](./solve/) for more details.

After decompiling the original pyc using a tool like `pycdc`, you'll see some base64 code that then get executed. If you reverse that process, you'll finally get to the meat of the challenge.

```py
check = lambda:None
code = type(check.__code__)(1, 0, 0, 6, 5, 67, b'|\x00d\x00d\x01\x85\x02\x19\x00d\x02k\x03r\x0et\x00j\x01j\x02d\x03\x19\x00S\x00|\x00d\x04\x19\x00d\x05k\x03r\x1at\x00j\x01j\x02d\x03\x19\x00S\x00|\x00d\x01d\x04\x85\x02\x19\x00}\x00t\x00j\x01j\x02d\x06\x19\x00|\x00\x83\x01d\x07k\x03r0t\x00j\x01j\x02d\x03\x19\x00S\x00g\x00}\x01t\x00j\x01j\x02d\x08\x19\x00|\x00\x83\x01D\x00]\r\\\x02}\x02}\x03|\x03d\tk\x02rG|\x01\xa0\x03|\x02\xa1\x01\x01\x00q:|\x01g\x00d\n\xa2\x01k\x03rTt\x00j\x01j\x02d\x03\x19\x00S\x00|\x00\xa0\x04\xa1\x00\xa0\x05d\x0b\xa1\x01}\x00|\x00d\x0c\x19\x00d\x00d\x00d\x04\x85\x03\x19\x00d\rk\x03rlt\x00j\x01j\x02d\x03\x19\x00S\x00|\x00d\x0e\x19\x00d\x0c\x19\x00|\x00d\x0e\x19\x00d\x0e\x19\x00\x17\x00|\x00d\x0e\x19\x00d\x0f\x19\x00\x18\x00|\x00d\x0e\x19\x00d\x0e\x19\x00|\x00d\x0e\x19\x00d\x0f\x19\x00\x17\x00|\x00d\x0e\x19\x00d\x0c\x19\x00\x18\x00|\x00d\x0e\x19\x00d\x0f\x19\x00|\x00d\x0e\x19\x00d\x0c\x19\x00\x17\x00|\x00d\x0e\x19\x00d\x0e\x19\x00\x18\x00f\x03d\x10k\x03r\xa9t\x00j\x01j\x02d\x03\x19\x00S\x00t\x00j\x01j\x02d\x11\x19\x00d\x12\x83\x01\xa0\x06|\x00d\x0f\x19\x00\xa1\x01\xa0\x07\xa1\x00d\x13k\x03r\xc0t\x00j\x01j\x02d\x03\x19\x00S\x00t\x00j\x01j\x02d\x11\x19\x00d\x14\x83\x01}\x04|\x04\xa0\x08|\x00d\x0f\x19\x00\xa1\x01\x01\x00t\x00j\x01j\x02d\x15\x19\x00|\x00d\x16\x19\x00\x83\x01|\x00d\x16<\x00|\x04\xa0\t|\x00d\x16\x19\x00\xa1\x01\x01\x00|\x00d\x16\x19\x00g\x00d\x17\xa2\x01k\x03r\xf0t\x00j\x01j\x02d\x03\x19\x00S\x00|\x00d\x18\x19\x00d\x19\x17\x00d\x1ak\x03r\xfet\x00j\x01j\x02d\x03\x19\x00S\x00t\x00j\x01j\x02d\x1b\x19\x00\xa0\n|\x00d\x1c\x19\x00d\x0cd\x18\x85\x02\x19\x00d\x1d\xa1\x02|\x04\xa0\x0bd\x0cd\x1e\xa1\x02A\x00d\x1fk\x03\x90\x01r\x1dt\x00j\x01j\x02d\x03\x19\x00S\x00t\x00j\x01j\x02d\x1b\x19\x00\xa0\n|\x00d\x1c\x19\x00d\x18d \x85\x02\x19\x00d\x1d\xa1\x02|\x04\xa0\x0bd\x0cd\x1e\xa1\x02A\x00d!k\x03\x90\x01r<t\x00j\x01j\x02d\x03\x19\x00S\x00t\x00j\x01j\x02d\x1b\x19\x00\xa0\n|\x00d\x1c\x19\x00d d\x01\x85\x02\x19\x00d"\x17\x00d\x1d\xa1\x02|\x04\xa0\x0bd\x0cd\x1e\xa1\x02A\x00d#k\x03\x90\x01r]t\x00j\x01j\x02d\x03\x19\x00S\x00d\x0c}\x05|\x00d$\x19\x00D\x00]\x0b}\x02|\x05d%9\x00}\x05|\x05|\x027\x00}\x05\x90\x01qct\x00j\x01j\x02d&\x19\x00|\x05\x83\x01d\'k\x03\x90\x01r\x80t\x00j\x01j\x02d\x03\x19\x00S\x00t\x00j\x01j\x02d(\x19\x00S\x00', (None, 12, 'amateursCTF{', 'False', -1, '}', 'len', 42, 'enumerate', '_', (7, 11, 13, 20, 23, 35), b'_', 0, b'sn0h7YP', 1, 2, (160, 68, 34), '__import__', 'hashlib', '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a', 'random', 'list', 3, (49, 89, 102, 109, 108, 52), 4, b'freebie', b'0ffreebie', 'int', 5, 'little', 4294967295, 4227810561, 8, 825199122, b'\x00', 4277086886, 6, 128, 'hex', '0x29ee69af2f3', 'True', 'Did you know? pycdc can decompile marshaled code objects. Just make sure you mention the right version!'), ('id', '__self__', '__dict__', 'append', 'encode', 'split', 'sha256', 'hexdigest', 'seed', 'shuffle', 'from_bytes', 'randint'), ('input', 'underscores', 'i', 'x', 'r', 'c'), '', 'check', 3, b'\x10\x01\x0c\x01\x0c\x01\x0c\x01\x0c\x01\x14\x02\x0c\x01\x04\x02\x18\x01\x08\x01\n\x01\x02\x80\x0c\x01\x0c\x01\x0e\x02\x16\x01\x0c\x01n\x03\x0c\x01"\x02\x0c\x01\x10\x02\x0e\x01\x18\x01\x0e\x01\x10\x02\x0c\x01\x10\x02\x0c\x012\x02\x0c\x012\x02\x0c\x016\x02\x0c\x01\x04\x02\x0c\x01\x08\x01\x0c\x01\x16\x02\x0c\x01\x0c\x02', (), ())

check = type(check)(code, {'id': id})
if check(input("Enter the flag: ")):
    print("Correct!")
else:
    print("Incorrect.")
```

This giant code block serves as the main checker for the flag. If you read the strings closely, you'll see that there's even a hint for what to do next.

So all we need to do now is dump using `marshal` and then use `pycdc` to decompile again
```py
import marshal

marshal.dump(code, open("check.pyc", "wb"))
# run pycdc on check.pyc
```

From here, we just need to satisfy all the conditions inside `check`:
```py
import hashlib
import random

def check(input):
    if input[:12] != 'amateursCTF{':
        return False
    if input[-1] != '}':
        return False
    input = input[12:-1]
    if len(input) != 42:
        return False
    
    underscores = None
    for i, x in enumerate(input):
        if x == '_':
            underscores.append(i)
    if underscores != [
            7,
            11,
            13,
            20,
            23,
            35]:
        return False

    input = input.encode().split(b'_')
    if input[0][::-1] != b'sn0h7YP':
        return False
    if (input[1][0] + input[1][1] - input[1][2], input[1][1] + input[1][2] - input[1][0], input[1][2] + input[1][0] - input[1][1]) != (160, 68, 34):
        return False
    if hashlib.sha256(input[2]).hexdigest() != '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a':
        return False

    random.seed(input[2])
    input[3] = list(input[3])
    random.shuffle(input[3])
    if input[3] != [
            49,
            89,
            102,
            109,
            108,
            52]:
        return False
    if input[4] + b'freebie' != b'0ffreebie':
        return False
    
    if int.from_bytes(input[5][0:4], 'little') ^ random.randint(0, 0xFFFFFFFF) != 0xFBFF4501:
        return False
    if int.from_bytes(input[5][4:8], 'little') ^ random.randint(0, 0xFFFFFFFF) != 825199122:
        return False
    if int.from_bytes(input[5][8:12] + b'\x00', 'little') ^ random.randint(0, 0xFFFFFFFF) != 0xFEEF2AA6:
        return False
    
    c = 0
    for i in input[6]:
        c *= 128
        c += i

    if hex(c) != '0x29ee69af2f3':
        return False
    return True
```

See [solve.py](./solve/solve.py) for the full solution.

flag: `amateursCTF{PY7h0ns_ar3_4_f4m1lY_0f_N0Nv3nom0us_Sn4kes}`