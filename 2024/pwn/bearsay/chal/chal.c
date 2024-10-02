#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <immintrin.h>
#include <unistd.h>
#include <fcntl.h>

const char *bears[] = {
    "ʕ •ᴥ•ʔ",
    "ʕ•ﻌ•`ʔ",
    "ʕ´•ᴥ•`ʔ",
    "ʕ •ɷ•ʔฅ",
};
#define NUMBEARS (sizeof(bears) / sizeof(bears[0]))
#define MAXLEN (4096)

int is_mother_bear = 0;

void rep(char ch, int count) {
    for (int i = 0; i < count; i++) {
        putchar(ch);
    }
}

void box(char side, char floor, int height, char *msg) {
    int len = strlen(msg);

    rep(floor, len + 4);
    putchar(10);
    for (int i = 0; i < height; i++) {
        putchar(side);
        rep(' ', len + 2);
        putchar(side);
        putchar(10);
    }
    putchar(side); putchar(0x20);
    printf(msg);
    putchar(0x20); putchar(side); putchar(10);
    for (int i = 0; i < height; i++) {
        putchar(side);
        rep(' ', len + 2);
        putchar(side);
        putchar(10);
    }
    rep(floor, len + 4);
    putchar(10);
}

int main(int argc, char *argv[]) {
    setbuf(stdout, NULL);

    srand(__rdtsc());

    while (1) {
        char input[MAXLEN];
        char *newline;

        printf("🧸 say: ");
        fgets(input, MAXLEN, stdin);

        if ((newline = strchr(input, 10))) {
            *newline = 0;
        }

        if (strlen(input) == 0) {
            printf("confused bear %s\n", bears[rand() % NUMBEARS]);
        } else if (strcmp("flag", input) == 0) {
            if (is_mother_bear == 0x0BAD0BAD) {
                char flag[MAXLEN];
                FILE *file = fopen("./flag.txt", "r");
                fgets(flag, MAXLEN, file);
                fclose(file);

                box('|', '-', 2, flag);

                printf("|\n|\n|\n");
                printf("%s\n", bears[rand() % NUMBEARS]);
            } else {
                printf("ANGRY BEAR %s\n", bears[rand() % NUMBEARS]);
                exit(1);
            }
        } else if (strcmp("leave", input) == 0) {
            printf("lonely bear... %s\n", bears[rand() % NUMBEARS]);
            exit(0);
        } else if (
            input[0] == 'm' &&
            input[1] == 'o' &&
            input[2] == 'o'
        ) {
            printf("no.\n");
            exit(1);
        } else {
            int len = strlen(input);

            box('*', '*', 0, input);

            rep(' ', len / 2);
            printf("|\n");

            const char *bear = bears[rand() % NUMBEARS];
            rep(' ', len / 2);
            printf("%s\n", bear);
        }
    }
}