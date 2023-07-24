#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int global_canary;

void win() {
    char buf[64];
    FILE *f = fopen("flag.txt", "r");
    if (f == NULL) {
        printf("flag file not found\n");
        exit(1);
    }
    fgets(buf, 64, f);
    puts(buf);
}

void generate_canary() {
    srand(time(NULL));
    global_canary = rand();
}

void random_guess() {
    printf("Enter in a number as your guess: ");
    int canary = global_canary;
    char buf[32];

    gets(buf);
    int guess = (int)strtol(buf, (char **)NULL, 10);

    if (canary != global_canary) {
        printf("***** Stack Smashing Detected ***** : Canary Value Corrupt!\n");
        exit(1);
    }

    if (guess == rand()) {
        printf("Congrats you guessed correctly!\n");
    } else {
        printf("Better luck next time\n");
    }
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    generate_canary();
    while (1) {
        printf("Please select one of the following actions\n");
        printf("1) Generate random number\n");
        printf("2) Try to guess a random number\n");
        printf("3) Exit\n");

        int option = 0;
        scanf("%d", &option);
        getchar();
        switch (option) {
        case 1:
            printf("%d\n", rand());
            break;
        case 2:
            random_guess();
            break;
        case 3:
            exit(0);
            break;
        }
    }
}