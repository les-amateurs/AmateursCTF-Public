#include "color.h"
#include <ctype.h>
#include <poll.h>
#include <setjmp.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/poll.h>
#include <unistd.h>

#define print(fmt, ...)                                                        \
    do {                                                                       \
        printf(fmt __VA_OPT__(, ) __VA_ARGS__);                                \
        /* fflush(stdout); */                                                  \
    } while (0);
#define println(fmt, ...) print(fmt "\n" __VA_OPT__(, ) __VA_ARGS__)
#define error(fmt, ...)                                                        \
    do {                                                                       \
        println("[!] " fmt __VA_OPT__(, ) __VA_ARGS__);                        \
        longjmp(handler, 1);                                                   \
    } while (0);

void iflush() {
    int ch = 0;
    do {
        ch = getc(stdin);
    } while (ch != '\n');
}

typedef struct {
    char *buf;
    size_t len;
} String;

typedef struct {
    String key;
    String val;
} Store;

#define DB_ENTRIES ((size_t)32)
Store db[DB_ENTRIES] = {0};
jmp_buf handler;

void readline(char *buf, size_t len) {
    char *ptr = buf;
    while (ptr < buf + len - 1) {
        int ch = getc(stdin);
        if (ch == '\n') {
            goto done;
        }
        *ptr++ = ch;
    }
    iflush();
done:
    *ptr = 0;
}

void db_line(String *string, int new, char *prompt) {
    if (new) {
        size_t len;
        print("len:\n>>> ");
        if (1 == scanf("%zu", &len)) {
            iflush();

            if (len == 0 || len >= 0x1000 - 8 || (len + 1) < len) {
                error("invalid line length");
            }

            len += 1;

            print("%s", prompt);

            char *buf = malloc(len);
            readline(buf, len);
            string->buf = buf;
            string->len = len;
            return;
        } else {
            iflush();
            error("failed to read length");
        }
    } else {
        print("%s", prompt);
        readline(string->buf, string->len);
    }
}

int db_menu() {
    int choice;
    println("");
    println("       =[ menu ]=");
    println("[1] => create key/value store");
    println("[2] => update key/value store");
    println("[3] => read   key/value store");
    println("[4] => delete key/value store");
    println("[5] => depart");
    print(">>> ");
    if (1 == scanf("%d", &choice)) {
        iflush();
        return choice;
    }
    iflush();
    error("failed to read choice");
}

int db_index(int check) {
    size_t idx;
    print("index:\n>>> ");
    if (1 == scanf("%zu", &idx)) {
        iflush();
        if (idx >= DB_ENTRIES) {
            error("index out of bounds");
        }
        if (check) {
            if (db[idx].key.buf == NULL || db[idx].val.buf == NULL) {
                error("invalid key/value store");
            }
        }
        return idx;
    } else {
        iflush();
        error("failed to read index");
    }
}

void db_println(String string) {
    for (size_t i = 0; i < string.len; i++) {
        if (isprint(string.buf[i])) {
            print("%c", string.buf[i]);
        } else {
            print("\\x%02x", (unsigned int)(unsigned char)string.buf[i]);
        }
    }
    print("\n");
}

void db_create() {
    int idx = db_index(0);
    db_line(&db[idx].key, 1, "key:\n>>> ");
    db_line(&db[idx].val, 1, "val:\n>>> ");
}

void db_update() {
    int idx = db_index(1);
    db_line(&db[idx].val, 0, "new val:\n>>> ");
}

void db_read() {
    int idx = db_index(1);
    print("key = ");
    db_println(db[idx].key);
    print("val = ");
    db_println(db[idx].val);
}

void db_delete() {
    int idx = db_index(1);

    free(db[idx].key.buf);
    free(db[idx].val.buf);
}

int main() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);

    println("##############################################");
    println("# WELCOME to the amateurs key/value database #");
    println("##############################################");

    while (1) {
        setjmp(handler);

        switch (db_menu()) {
        case 1:
            println("\n       =[ create ]=");
            db_create();
            break;
        case 2:
            println("\n       =[ update ]=");
            db_update();
            break;
        case 3:
            println("\n       =[ read ]=");
            db_read();
            break;
        case 4:
            println("\n       =[ delete ]");
            db_delete();
            break;
        case 5:
            return 0;
        default:
            println("[!] invalid selection");
            continue;
        }
    }
}