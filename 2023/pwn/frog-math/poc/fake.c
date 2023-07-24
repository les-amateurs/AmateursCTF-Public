#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

int main() {
    uint64_t __attribute__((aligned(0x20))) fake[64];
    fake[0] = 0;
    fake[1] = 0x91;
    void * chunk = fake + 2;
    printf("fake: %p\n", chunk);
    
    void *ptrs[7];
    for (int i = 0; i < 7; i++)
        ptrs[i] = malloc(0x88);
    for (int i = 0; i < 7; i++)
        free(ptrs[i]);
    free(chunk);
}