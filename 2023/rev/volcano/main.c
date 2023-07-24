#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#define ull unsigned long long

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

bool is_bear(ull x){
    if (x % 2 != 0) return false;
    if (x % 3 != 2) return false;
    if (x % 5 != 1) return false;
    if (x % 7 != 3) return false;
    if (x % 109 != 55) return false;   
    return true;
}

bool is_volcano(ull x){
    ull c = 0;
    ull t = x;
    while (t){
        c += t & 1;
        t >>= 1;
    }
    if (c < 17) return false;
    if (c > 26) return false;
    return true;
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

int main(){
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    printf("Give me a bear: ");
    ull bear = 0;
    scanf("%llu", &bear);
    if (!is_bear(bear)){
        printf("That doesn't look like a bear!\n");
        return 1;
    }

    printf("Give me a volcano: ");
    ull volcano = 0;
    scanf("%llu", &volcano);
    if (!is_volcano(volcano)){
        printf("That doesn't look like a volcano!\n");
        return 1;
    }

    printf("Prove to me they are the same: ");
    ull m = 0;
    ull secret = 0x1337;
    scanf("%llu", &m);
    if (m % 2 != 1 || m == 1){
        printf("That's not a valid proof!\n");
        return 1;
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
    printf("Nope that's not right!\n");
    return 1;
}