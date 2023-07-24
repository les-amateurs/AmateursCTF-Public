#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <err.h>
#include <string.h>
#include <execinfo.h>


void * getchunk() {
    size_t size;
    printf("size: ");
    scanf("%lu", &size);
    getchar();
    printf("data: ");
    char * chunk = malloc(size);
    char * part = chunk;
    while (size > 0) {
        size_t status = read(0, part, size);
        if (status < 0) {
            errx(1, "failed to read data");
        }
        size -= status;
        part += status;
    }
    return chunk;
}

void check(char * guess) {
    char * flag = malloc(128);
    int fd = open("flag.txt", O_RDONLY);
    if (fd < 0) {
        errx(1, "failed to open flag.txt");
    }
    read(fd, flag, 128);
    close(fd);
    if (strcmp(guess, flag) == 0) {
        puts("Correct!");
        exit(7);
    } else {
        printf("%s is not the flag.\n", guess);
    }
    free(flag);
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    puts("Welcome to the flag checker");

    void * first = getchunk();
    
    puts("I'll give you three chances to guess my flag.");
    char * second = getchunk();
    check(second);

    puts("I'll also let you change one character");
    int index;
    printf("index: ");
    scanf("%d", &index);
    getchar();
    printf("new character: ");
    char new = getchar();
    getchar();
    *(second + index) = new;
    check(second);

    free(second);

    puts("Last chance to guess my flag");
    char * third = getchunk();
    check(third);

    asm goto("" :::: afterword);

    exit(0);

afterword:
    puts("no");
    fputs("/bin/sh", stdout);
    write(1, "for you\n", sizeof("for you\n"));
    putchar('.');
    fputc('\n', stdout);
}