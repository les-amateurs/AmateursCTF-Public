# rusteze

## Author: flocto

**Solves:** 79

**Points:** 449

---

Get rid of all your Rust rust with this brand new Rust-eze™ de-ruster.

Flag is `amateursCTF{[a-zA-Z0-9_]+}`

---

**Provided Files:**

- [rusteze](./rusteze)

## Solution

While this is a Rust rev, symbol names are left in, so finding `main` is really easy. 

After locating `main`, the two static arrays are easy to find, and its also not too hard to tell that the latter is used in the final comparison to determine if the input is correct.

As for the first array, the loop that acts on it seems pretty long, but staring between the Rust panics, we see the logic boils down to:
```rust
for i in 0..38 {
    temp[i] = input[i] ^ arr1[i];
    temp[i] = temp[i].rotate_left(2);
}
```

So, we can just reverse this rotate and xor, and get the flag:
```py
enc = [25, 235, 216, 86, 51, 0, 80, 53, 97, 220, 150, 111, 181, 13, 164, 122, 85, 232, 254, 86, 151, 222, 157, 175, 212, 71, 175, 193, 194, 106, 90, 172, 177, 162, 138, 89, 82, 226]
arr = [39, 151, 87, 225, 169, 117, 102, 62, 27, 99, 227, 160, 5, 115, 89, 251, 10, 67, 143, 224, 186, 192, 84, 153, 6, 191, 159, 47, 196, 170, 166, 116, 30, 221, 151, 34, 237, 197]

def rotate(x):
    bot = x & 0b11
    return (x >> 2) | (bot << 6)

for i, e in enumerate(enc):
    print(chr(rotate(e) ^ arr[i]), end='')
print()
```

flag: `amateursCTF{h0pe_y0u_w3r3nt_t00_ru5ty}`