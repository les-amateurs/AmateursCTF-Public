#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

int main() {
    char buf[16];
    static char guess[] = { 0, 'g', 'u', 'e', 's', 's', 0x69, 0x42, 0xaa, 0xaa, 0, 'A', 'B', 'C', 'D' };

    setbuf(stdout, NULL);
    setbuf(stdin, NULL);

    while (1) {
        printf("guess = ");
        fgets(buf, 16, stdin);
        if (memcmp(buf, guess, sizeof(guess)) == 0) {
            char flag[64] = {0};
            int fd = open("flag.txt", O_RDONLY);
            read(fd, flag, 63);
            printf("here you go: %s\n", flag);
            exit(0);
        }
        printf(buf);
    }
}