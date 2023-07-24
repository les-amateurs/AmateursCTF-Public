# volcano

## Author: flocto

**Solves:** 208

**Points:** 329

---

Inspired by recent "traumatic" events.

`nc amt.rs 31010`

---

**Provided Files:**

- [volcano](./volcano)

## Solution
To solve this challenge, you just need to find 3 numbers that satisfy the following conditions:
- The first number must pass the `is_bear` check
- The second number must pass the `is_volcano` check
- Both numbers have to be proved "equivalent" through a series of checks

The first check for a `bear`, is easy to reverse. Though the instructions may seem a bit confusing, it's actually just how modulo is optimized in assembly. In reality, the check just looks like:
```c
bool is_bear(ull x){
    if (x % 2 != 0) return false;
    if (x % 3 != 2) return false;
    if (x % 5 != 1) return false;
    if (x % 7 != 3) return false;
    if (x % 109 != 55) return false;   
    return true;
}
```
So we can easily find bears through CRT or just by brute forcing

The second check for a `volcano` just checks if the number has between 17 and 26 bits.
```c
bool is_volcano(ull x){
    ull c = 0;
    ull t = x;
    while (t){ // count the bits
        c += t & 1;
        t >>= 1;
    }
    if (c < 17) return false;
    if (c > 26) return false;
    return true;
}
```

Finally, to prove the two numbers are equal, first they have to be the same length as well as have the same digit sum. If so, then a third number $m$ has to be entered such that
$$
\text{secret} = \text{0x}1337 \\
\text{secret}^\text{bear} \mod m \equiv \text{secret}^\text{volcano} \mod m
$$
Here's the code for that check:
```c
ull length(ull x){
    ull c = 0;
    for (; x; x /= 10) c++;
    return c;
}

ull sum(ull x){
    ull c = 0;
    while (x){
        c += x % 10;
        x /= 10;
    }
    return c;
}
ull mod_exp(ull x, ull y, ull p){
    ull res = 1;
    x = x % p;
    while (y > 0){
        if (y & 1) res = (res * x) % p;
        y = y >> 1;
        x = (x * x) % p;
    }
    return res;
}

if (length(volcano) == length(bear)){
    if(sum(volcano) == sum(bear)){
        if (mod_exp(secret, volcano, m) == mod_exp(secret, bear, m)){
            printf("That looks right to me!\n");
            FILE *f = fopen("flag.txt", "r");
            char buf[128];
            fgets(buf, 128, f);
            printf("%s\n", buf);
            return 0;
        }
    }
}
```

From here, we can just write a simple brute-forcer to generate valid volcanoes and bears, then find an $m$ that satisfies the equation. 
See my solution inside [solve.py](./solve.py). You can also look for a number that is both a volcano and a bear, since then any value of $m$ is valid.

flag: `amateursCTF{yep_th0se_l00k_th3_s4me_to_m3!_:clueless:}`