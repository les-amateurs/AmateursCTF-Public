#include <stdio.h>
#include <stdlib.h>

unsigned char x = 0, y = 0;
unsigned char board[] = {0x8b, 0xc9, 0x92, 0x8, 0xf9, 0x91, 0xd6, 0xc8};
unsigned char flag[] = {0xd6, 0xb2, 0x5, 0x20, 0x95, 0x5b, 0x1a, 0xbe, 0x4e, 0x70, 0x5f, 0x60, 0xf9, 0x74, 0x51, 0xee, 0x69, 0x56, 0x8c, 0x6a, 0xc1, 0x00};
unsigned char moves[28] = { 0 };
unsigned char *movep = moves;

int main() {
    for (int i = 0; i < 28;) {
        printf("> ");
        char move;
        do {
            move = getchar();
        } while (move == '\n');

        if (move == 'w') {
            y--;
            *movep++ = 0;
        } else if (move == 'a') {
            x--;
            *movep++ = 1;
        } else if (move == 's') {
            y++;
            *movep++ = 2;
        } else if (move == 'd') {
            x++;
            *movep++ = 3;
        }
        else continue;
        
        x &= 7;
        y &= 7;
        board[y] ^= 1 << x;
        i++;
    }

    for (int i = 0; i < 8; i++) {
        srand(0xdeadbeef + 0x1337 * i);
        if ((rand() & 0xff) != board[i]) {
            printf("you fell into lava\n");
            return 0;
        }
    }

    unsigned long long seed = 0;
    for (int i = 0; i < 28; i++) {
        seed = (seed << 2) | moves[i];
    }

    srand(*((unsigned int *) (&seed)) ^ ((unsigned int *) (&seed))[1]);
    for (int i = 0; i < sizeof(flag) - 1; i++) {
        flag[i] ^= rand() & 0xff;
    }

    printf("you made it across!\n");
    printf("here's your reward:\n");
    printf("amateursCTF{%s}\n", flag);
}
