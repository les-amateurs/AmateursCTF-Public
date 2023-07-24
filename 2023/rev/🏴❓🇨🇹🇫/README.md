# 🏴❓🇨🇹🇫

## Author: flocto

**Solves:** 19

**Points:** 490

---

I apologize in advance. Flag is `amateursCTF{[a-z0-9_]+}`

Compiled using the latest version of [emojicode](https://www.emojicode.org/)

Note that there may be multiple inputs that cause the program to print ✅. 
The correct input (and the flag) has sha256 hash `53cf379fa8fd802fd2f99b2aa395fe8b19b066ab5e2ff49e44633ce046c346c4`.

---

**Provided Files:**

- [emojis.tar.gz](./emojis.tar.gz)


## Solution

The emojicode logic reimplements a nonogram checker, with the two large lists of lists being the nonogram hints.

Plug them into any nonogram solver and get the flag in truncated ASCII binary.

I used [this](http://www.landofcrispy.com/nonogrammer/nonogram.html?mode=solve) and [this](https://return.co.de/gridsolver/) while testing, both work fine.

The resulting grid should look like:
```
1100001110110111
0000111101001100
1011110101111001
0111001110000111
0101001000110111
1011110111110100
0110100111100111
0111111100010110
0101110110011011
1111011101100111
1110011101111111
0100111011101110
0111100011100100
1100101101111111
0110111010011101
0111000111111101
```
As binary
```
1100001110110111000011110100110010111101011110010111001110000111010100100011011110111101111101000110100111100111011111110001011001011101100110111111011101100111111001110111111101001110111011100111100011100100110010110111111101101110100111010111000111111101
```

then just use [this cool bruteforcer](https://potatosfield.neocities.org/tools/binary/binary-choice) to guess the flag letter by letter to get a sensible message (and to pass the hash).

flag: `amateursCTF{7his_belongs_ins1de_mi5c}`