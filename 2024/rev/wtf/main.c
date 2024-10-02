#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define N 12

static uint64_t matrix[N][N];
static uint64_t MOD = 1000000007;

void __attribute__((constructor)) init() {
    // 6775411 1702260588 6775660 15797360
    uint64_t a = 6775411;
    uint64_t b = 1702260588;
    uint64_t c = 6775660;
    uint64_t seed = 15797360;
    uint64_t tmp = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            tmp = a;
            tmp = (tmp * seed + b) % MOD;
            seed = (tmp * seed + c) % MOD;
            matrix[i][j] = seed;
        }
    }
}

void matrix_mul(uint64_t a[N][N], uint64_t b[N][N]) {
    uint64_t c[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            c[i][j] = 0;
            for (int k = 0; k < N; k++) {
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD;
            }
        }
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            a[i][j] = c[i][j];
        }
    }
}

void inc(uint8_t num[30]){
    uint64_t i = 29;
    while(num[i] == 255) {
        num[i] = 0;
        i--;
    }
    num[i]++;
}

uint8_t checkmat(uint64_t a[N][N]){
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            if(i == j && a[i][j] != 1) {
                return 0;
            }
            if(i != j && a[i][j] != 0) {
                return 0;
            }
        }
    }
    return 1;
}

void checkflag(uint8_t num[30]){
    uint64_t a[N][N];
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            a[i][j] = matrix[i][j];
        }
    }

    while(!checkmat(a)) {
        inc(num);
        matrix_mul(a, matrix);
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Please provide a flag\n");
        return 1;
    }

    char* flag = argv[1];
    if(strlen(flag) != 43) {
        fail:
        printf("Wrong!\n");
        return 1;
    }
    if(strncmp(flag, "amateursCTF{", 12) != 0) {
        goto fail;
    }
    if(flag[42] != '}') {
        goto fail;
    }

    // c4ac23183333133c9ffadaf4d199170b81aaea279d4a450679b9f13b17b4
    char enc[30] = "\xc4\xac\x23\x18\x33\x33\x13\x3c\x9f\xfa\xda\xf4\xd1\x99\x17\x0b\x81\xaa\xea\x27\x9d\x4a\x45\x06\x79\xb9\xf1\x3b\x17\xb4";
    uint8_t num[30] = {0};
    checkflag(num);
    
    for(int i = 0; i < 30; i++) {
        enc[i] ^= num[i];
    }

    if(strncmp(enc, flag + 12, 30UL) == 0) {
        printf("Correct!\n");
    } else {
        goto fail;
    }

    return 0;
}
