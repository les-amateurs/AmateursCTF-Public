#include <stdio.h>
#include <stdlib.h>

static size_t mod = 1000000007;

size_t inc(size_t c) {
    size_t mask = 1;
    while (c & mask) {
        mask <<= 1;
    }

    c |= mask;
    while (mask >>= 1) {
        c &= ~mask;
    }

    return c;
}

size_t add(size_t a, size_t b) {
    for (size_t c = 0; c < b; c = inc(c)) {
        a = inc(a);
    }
    return a % mod;
}

size_t fast_op(size_t a, size_t b, size_t r, size_t(op)(size_t, size_t)) {
    while (b) {
        if (b & 1) {
            r = op(r, a) % mod;
        }
        a = op(a, a) % mod;
        b >>= 1;
    }
    return r;
}

// size_t add_fast(size_t a, size_t b) {
//     return (a + b) % mod;
// }

// size_t mul_fast(size_t a, size_t b) {
//     return (a * b) % mod;
// }

// size_t pmul_fast(size_t a, size_t b) {
//     return fast_op(a, b, 1, mul_fast);
// }

size_t mul(size_t a, size_t b) {
    return fast_op(a, b, 0, add);
    // return fast_op(a, b, 0, add);
}

size_t pmul(size_t a, size_t b) {
    return fast_op(a, b, 1, mul);
}

int main() {
    char s[64];
    fgets(s, 64, stdin);

    unsigned char r[2];
    FILE *f = fopen("/dev/urandom", "r");
    fread(r, 1, 2, f);
    fclose(f);

    size_t x = 0;
    for (size_t i = 0; s[i]; ++i) {
        x = add(x, s[i]);
        x = mul(x, r[0]);
        x = pmul(x, r[1]);
        // x = add_fast(x, s[i]);
        // x = mul_fast(x, r[0]);
        // x = pmul_fast(x, r[1]);
        if (i != 0)
            printf(", ");
        printf("%zu", x);
    }

    printf("\n");
    return 0;
}