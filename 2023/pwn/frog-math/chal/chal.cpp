#include <cstdio>
#include <cstdlib>
#include <immintrin.h>
#include <cstdint>
#include <iostream>
#include <iomanip>

using namespace std;

void push(long double v) {
    __asm__ __volatile__("fld tbyte ptr [%[v]]" :: [v] "r" (&v));
}

void pop() {
    __asm__ __volatile__("fincstp");
}

void add() {
    __asm__ __volatile__("fadd st(0), st(1)");
}

void sub() {
    __asm__ __volatile__("fsub st(0), st(1)");
}

void mul() {
    __asm__ __volatile__("fmul st(0), st(1)");
}

void div() {
    __asm__ __volatile__("fdiv st(0), st(1)");
}

void fxsave(char * buf) {
    __asm__ __volatile__("fxsave [%[buf]]" :: [buf] "r" (buf));
}

void fxload(char * buf) {
    __asm__ __volatile__("fxrstor [%[buf]]" :: [buf] "r" (buf));
}

int depth = 0;

void do_x87() {
    _mm_empty();

    while (true) {
        puts("fp processing");
        puts("0) finish");
        puts("1) push");
        puts("2) pop");
        puts("3) add");
        puts("4) sub");
        puts("5) mul");
        puts("6) div");
        puts("7) inspect");
        printf("> ");

        char buf[512];
        int choice;

        cin >> choice;

        switch (choice) {
            case 0:
                return;
            case 1:
                if (depth < 7) {
                    fxsave(buf);
                    long double value;
                    cin >> value;
                    fxload(buf);
                    push(value);
                    depth += 1;
                } else {
                    puts("fp stack limit reached");
                }
                break;
            case 2:
                if (depth > 0) {
                    pop();
                    depth -= 1;
                } else {
                    puts("fp stack already empty");
                }
                break;
            case 3:
                add();
                break;
            case 4:
                sub();
                break;
            case 5:
                mul();
                break;
            case 6:
                div();
                break;
            case 7: {
                fxsave(buf);
                char * val = buf + 32;
                printf("%Lf %lu\n", *(long double *)(val), *(uint64_t *)(val));
                fxload(buf);
                break;
            }
            default:
                puts("try again");
                break;
        }
    }
}

register uint64_t mm0 asm("mm0");
register uint64_t mm1 asm("mm1");
register uint64_t mm2 asm("mm2");
register uint64_t mm3 asm("mm3");
register uint64_t mm4 asm("mm4");
register uint64_t mm6 asm("mm6");
register uint64_t mm5 asm("mm5");
register uint64_t *mm7 asm("mm7");

uint64_t get(int i) {
    switch (i) {
        case 0:
            return mm0;
        case 1:
            return mm1;
        case 2:
            return mm2;
        case 3:
            return mm3;
        case 4:
            return mm4;
        case 5:
            return mm5;
        case 6:
            return mm6;
        default:
            return 0;
    }
}

void set(int i, size_t v) {
    switch (i) {
        case 0:
            mm0 = v;
            break;
        case 1:
            mm1 = v;
            break;
        case 2:
            mm2 = v;
            break;
        case 3:
            mm3 = v;
            break;
        case 4:
            mm4 = v;
            break;
        case 5:
            mm5 = v;
            break;
        case 6:
            mm6 = v;
            break;
        default:
            break;
    }
}

void do_mmx() {
    while (true) {
        puts("integer processor");
        puts("0) finish");
        puts("1) set");
        puts("2) get");
        puts("3) add");
        puts("4) sub");
        puts("5) mul");
        puts("6) div");
        puts("7) load");
        puts("8) save");
        puts("9) clear");
        printf("> ");

        int choice;
        size_t a, b;

        cin >> choice;
        switch (choice) {
            case 0:
                return;
            case 1:
                cin >> a >> b;
                set(a, b);
                break;
            case 2:
                cin >> a;
                printf("%lu\n", get(a));
                break;
            case 3:
                cin >> a >> b;
                set(a, get(a) + get(b));
                break;
            case 4:
                cin >> a >> b;
                set(a, get(a) - get(b));
                break;
            case 5:
                cin >> a >> b;
                set(a, get(a) * get(b));
                break;
            case 6:
                cin >> a >> b;
                set(a, get(a) / get(b));
                break;
            case 7:
                if (mm7 != NULL) {
                    mm0 = *(mm7);
                    mm1 = *(mm7 + 1);
                    mm2 = *(mm7 + 2);
                    mm3 = *(mm7 + 3);
                    mm4 = *(mm7 + 4);
                    mm5 = *(mm7 + 5);
                    mm6 = *(mm7 + 6);
                    free(mm7);
                    mm7 = NULL;
                } else {
                    puts("no state to load");
                }
                break;
            case 8: {
                if (mm7 == NULL) {
                    mm7 = (uint64_t *)malloc(7 * 8);
                }
                *(mm7) = mm0;
                *(mm7 + 1) = mm1;
                *(mm7 + 2) = mm2;
                *(mm7 + 3) = mm3;
                *(mm7 + 4) = mm4;
                *(mm7 + 5) = mm5;
                *(mm7 + 6) = mm6;
                break;
            }
            default:
                puts("try again");
                break;
        }
    }
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
    cout.rdbuf()->pubsetbuf(0, 0);
    cin.rdbuf()->pubsetbuf(0, 0);

    mm7 = NULL;

    puts("Welcome to the frog math calculation facility");
    puts("Here we provide state of the art processors for fp and integer math");

    while (true) {
        puts("0) exit");
        puts("1) floating point");
        puts("2) integer");
        printf("> ");

        int choice;
        cin >> choice;
        switch (choice) {
            case 0:
                exit(0);
            case 1:
                do_x87();
                break;
            case 2:
                do_mmx();
                break;
        }
    }
}