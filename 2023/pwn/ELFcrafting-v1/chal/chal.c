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

    printf("I'm sure you all enjoy doing shellcode golf problems.\n");
    printf("But have you ever tried ELF golfing?\n");
    printf("Have fun!\n");

    int fd, ok;
    char buffer[32];

    try(fd = memfd_create("golf", 0));
    
    try(ok = read(0, buffer, 32));
    printf("read %d bytes from stdin\n", ok);
    
    try(ok = write(fd, buffer, ok));
    printf("wrote %d bytes to file\n", ok);
    
    try(fexecve(fd, argv, envp));
}
