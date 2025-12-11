#include <stdio.h>

int main(void) {
    const char *path = "/flag.txt";
    FILE *fp = fopen(path, "r");

    if (!fp) {
        perror("fopen");
        return 1;
    }

    int c;
    while ((c = fgetc(fp)) != EOF) {
        putchar(c);
    }

    fclose(fp);
    return 0;
}
