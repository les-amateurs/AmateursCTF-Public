# rusteze 2

## Author: flocto

**Solves:** 20

**Points:** 489

---

My boss said Linux binaries wouldn't reach enough customers so I was forced to make a Windows version.

Flag is `amateursCTF{[a-zA-Z0-9_]+}`

---

**Provided Files:**

- [rusteze-2.exe](./rusteze-2.exe)

## Solution
Without symbols, locating `main` is a little harder this time, but still not too bad if you look for strings or follow the general Rust call chain to main.

Inside `main`, you'll notice the loops have changed a bit but the overall logic is still:
```
def enc(inp):
    temp = [0] * 35
    for i in 0..35:
        temp[i] = inp[i] ^ arr1[i]
        temp[i] = temp[i].rotate_left(2)
    return temp

def main():
    input = get_input()
    if len(input) != 35:
        print("Wrong!")
        return
    
    temp = enc(input)
    if temp != arr2:
        print("Wrong!")
        return
    
    print("Correct!")
```

However, if you use the decryption process as before, you get a fake string `sorry_this_isnt_the_flag_this_time.`, so we have to look a little deeper.

Going back to the encryption functionality, if you look closely, you'll notice a strange xor that never gets used:
```c
    local_39 = *(byte *)(param_2 + uVar3) ^ local_93[uVar3]; // right here

    if (uVar3 < 0x1e) { // rust panic stuff
      if (0x1d < uVar3) {
        FUN_140023bf0(uVar3,0x1e,&PTR_s_src\main.rs_140025678);
        goto LAB_140002b5d;
      }
      bVar1 = (&DAT_140030000)[uVar3];
      (&DAT_140030000)[uVar3] = local_39 ^ bVar1;
      uVar3 = CONCAT71((int7)(uVar3 >> 8),local_39 ^ bVar1);
    }

    // rest of encryption logic below
```

This is where the actual real flag is, so by performing this additional extra xor, we can get the flag:
```py
item = b'\xc0\xa7\xe5\xb7\x03\x46\x35\x26\xae\x1a\x37\xd4\x98\xda\x39\x17\x88\xe3\x7d\x8f\xf2\xae\x19\x49\x0e\xdc\xe9\x36\x82\x5f'
stuff = [
   0xd2, 0xa5, 0xf6, 0xb1, 0x1f, 0x6c, 0x33, 0x3d, 0x84, 0x3d, 0x2e, 0xc6, 0x8f, 0x84, 0x23, 0x7b, 0xa3, 0xbf, 0x76, 0xb4, 0xcb, 0xa6, 0x1d, 0x7c, 0x24, 0xdb, 0xf5, 0x6c, 0x95, 0x7d, 0x56, 0x61, 0x85, 0x4d, 0x2f
]

fill = b'sorry_this_isnt_the_flag_this_time.'

flag = bytes([fill[i] ^ stuff[i] ^ item[i] for i in range(len(item))])
print(flag)
```

flag: `amateursCTF{d0n3_4nd_deRust3d}`
