# flagchecker

## Author: flocto, hellopir2

**Solves:** 20

**Points:** 489

---

I was making this simple flag checker in Scratch, but my friend logged into my account and messed up all my variable names :(.
Can you help me recover my flag please? 

You should run on [Turbowarp](https://turbowarp.org/) for better performance.

---

**Provided Files:**

- [flagchecker.sb3](./flagchecker.sb3)

## Solution
You can reverse engineer a lot, but the key things to notice are:

- At the start, 4 numbers get added to some static variable.
- The encrypted flag is hardcoded:
```
239 202 230 114 17 147 199 39 182 230 119 248 78 246 224 46 99 164 112 134 30 216 53 194 60 75 223 122 67 202 207 56 16 128 216 142 248 16 27 202 119 105 158 232 251 201 158 69 242 193 90 191 63 96 38 164
```
- The constant 0x9E3779B9 is used in some sort of "main" loop that runs many times throughout the program.

These 3 things, especially the last one, should hint towards the [Tiny Encryption Algorithm, or TEA](https://en.wikipedia.org/wiki/Tiny_Encryption_Algorithm), which is in fact what this program does. It just encrypted the input with a hardcoded key, and compares it to the hardcoded encrypted flag.

We can easily reverse the encryption, and get the flag.
```python
# see full TEA implementation details in solve.py
from Crypto.Util.number import bytes_to_long, long_to_bytes

key = [69420, 1412141, 1936419188, 1953260915]

enc = open("data.txt", "r").read().strip().splitlines() # exfil data from scratch project
enc = [int(i) for i in enc]
enc = bytes(enc)
print(enc)
msg = b''
for i in range(0, len(enc), 8):
    block = enc[i:i+8]
    v = [bytes_to_long(block[:4]), bytes_to_long(block[4:])]
    block = decipher(v, key)
    msg += long_to_bytes(block[0]) + long_to_bytes(block[1])
    
print(msg)
```

Full flag: `amateursCTF{screw_scratch_llvm_we_code_by_hand_1a89c87b}`