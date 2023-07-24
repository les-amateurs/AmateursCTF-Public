# jvm

## Author: flocto

**Solves:** 27

**Points:** 485

---

I heard my professor talking about some "Java Virtual Machine" and its weird gimmicks, so I took it upon myself to complete one. It wasn't even that hard? I don't know why he was complaining about it so much.

Compiled with `openjdk 11.0.19`.

Run with `java JVM code.jvm`.

---

**Provided Files:**

- [jvm.tar.gz](./jvm.tar.gz)
- [code.jvm](./code.jvm)

## Solution
This is a pretty basic-ish VM rev, just analyze the code, write your own parser, blah blah blah. 
Sorry that it's a bit boring, but I felt like a pretty easy VM challenge was good for HS-level.

The only few hiccups I threw in here are:
- Loading in the flag length by doubling 10 twice and adding 5:
  $10 \rArr 20 \rArr 40 \rArr 45$
- Loading the check for `A` through a similar doubling process like before.
  
Other than that, every character is checked either by loading the exact value onto the stack and checking if equal, or by loading a random offset, adding it to the inputted character, and checking if that is equal to a constant.

Because of that, you can in fact solve the challenge like this:
```python
code = open("code.jvm", "rb").read()

segments = code.split(b'5')[1:] # 5 is pop

flag = ''
for s in segments:
    print(s, len(s))
    if len(s) < 10:
        flag = chr(s[3]) + flag
    elif len(s) == 10:
        offset = s[3]
        flag = chr(s[6] + offset) + flag
    else:
        flag = 'A' + flag
print(flag)
```
Obviously a very hindsight solution, but it works xd. Feel free to share your own parsers if you wrote any!

Full flag: `amateursCTF{wh4t_d0_yoU_m34n_j4v4_isnt_A_vm?}`