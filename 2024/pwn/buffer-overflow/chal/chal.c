#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include <err.h>
#include <string.h>
#include <stdlib.h>

extern void uppercase(char *src, size_t len, char *dst);

#define BUFLEN 4096

int main() {
    ssize_t bytes;
    size_t len;
    char *newline;
    char buf[BUFLEN] = {0};

    bytes = read(0, buf, BUFLEN);
    if (0 > bytes) {
        errx(1, "failed to read input");
    }

    buf[bytes - 1] = 0;
    newline = strchr(buf, '\n');
    if (newline) {
        *newline = 0;
        len = newline - buf;
    } else {
        len = bytes - 1;
    }

    uppercase(buf, len, buf);
    puts(buf);
}

__attribute__((aligned(0x20)))
void win() {
    system("/bin/sh");
}