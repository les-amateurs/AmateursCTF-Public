#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern int headache(char *);

int main() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    printf("Enter flag: ");
    char input[0x100];
    scanf("%s", input);

    if(strlen(input) != 61){
        printf("Wrong!\n");
        return 0;
    }

    int status = headache(input);
    if(status){
        printf("Correct!\n");
    }
    else{
        printf("Wrong!\n");
    }
    return 0;
}