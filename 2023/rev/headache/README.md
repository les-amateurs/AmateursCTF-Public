# headache

## Author: flocto, unvariant

**Solves:** 44

**Points:** 474

---

Ugh... my head hurts...
Flag is `amateursCTF{[a-zA-Z0-9_]+}`

---

**Provided Files:**

- [headache](./headache)

## Solution
This one is actually not that bad once you get past the initial decompilation and analysis.

Here's the first layer of the check function:
```c
00401290  uint64_t sub_401290(void* arg1)
00401290  {
0040129b      if ((*(int8_t*)((char*)arg1 + 0x19) ^ *(int8_t*)arg1) != 0x56)
00401297      {
004012a3          return 0;
004012a3      }
00404379      int32_t* rsi = sub_4012a4;
0040438a      do
0040438a      {
00404381          *(int32_t*)rsi = (*(int32_t*)rsi ^ 0xea228de6);
00404383          rsi = &rsi[1];
00404383      } while (rsi[-1] != 0xea228de6);
00404391      int64_t rcx;
00404391      int64_t rdx;
00404391      void* rbx;
00404391      int32_t rbp;
00404391      return sub_4012a4(arg1, rsi, rdx, rcx, 0xe6, rbx, rbp);
0040438c  }
```
I've left the addresses in, since after the initial xor check, you can see a HUGE jump to an address almost 0x3000 away. 

The next part xors the bytes with a fixed int right after the xor check code, then calls those xorred bytes as functions.

If you manually xor the next few sections, you'll start to notice a pattern of xor check, jump, xor bytes, then call bytes.
This pattern largely remains the same throughout, meaning you can build a parser to automate the process and store all the xor checks together.

The only few exceptions to the pattern occur when the index in the xor check is 0, which is a simple check, and when the jump to the xor bytes section is small enough to change the instruction. See [solve.py](solve.py) for full explanation.

Anyway, after repeating this process (hopefully manually) and gathering all 200ish xor checks, you can just toss them into z3 and force the first letter to be `a`, and get the flag.
```python
import z3
s = z3.Solver()

length = 0x3d
flag = [z3.BitVec(f"flag_{i}", 8) for i in range(length)]

for a, b, c in conditions:
    s.add(flag[a] ^ flag[b] == c)

s.add(flag[0] == b'a'[0])

if s.check() == z3.sat:
    m = s.model()
    flag = "".join([chr(m[f].as_long()) for f in flag])
    print(flag)
```

Full flag: `amateursCTF{i_h4v3_a_spli77ing_headache_1_r3qu1re_m04r_sl33p}``