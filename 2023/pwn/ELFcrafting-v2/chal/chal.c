#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdint.h>
#include <string.h>

typedef uint64_t u64;
typedef uint32_t u32;
#define try(expr) { \
    if (0 > (expr)) { \
        perror("failed to execute "#expr); \
        exit(1); \
    } \
}

int main (int argc, char * const argv[], char * const envp[]) {
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    printf("I've patched the (intended) unintended solves from the previous version\n");
    printf("Do you still have what it takes to solve the challenge?\n");
    printf("Have fun! :D\n");

    int fd, ok;
    char magic[4] = { 0x7F, 'E', 'L', 'F', };
    char buffer[79];

    try(fd = memfd_create("golf", 0));
    
    try(ok = read(0, buffer, 79));
    printf("read %d bytes from stdin\n", ok);
    if (memcmp(magic, buffer, 4) != 0) {
        printf("not an ELF file :/\n");
        exit(1);
    }
    
    try(ok = write(fd, buffer, ok));
    printf("wrote %d bytes to file\n", ok);
    
    try(fexecve(fd, argv, envp));
}
