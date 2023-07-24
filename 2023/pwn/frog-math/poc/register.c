#include <stdio.h>
#include <stdlib.h>

void a() {
    printf("handler called\n");
    exit(0);
}

void b() {
    printf("arginfo called\n");
    exit(0);
}

int main() {
    printf("%lu\n", 0);
    register_printf_function('u', a, b);
    printf("%lu\n", 0);
}