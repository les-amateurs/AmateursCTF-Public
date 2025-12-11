#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LOGIN_SIZE 0x200
#define NAME_SIZE 0x100
#define PASS_SIZE LOGIN_SIZE - NAME_SIZE

typedef struct {
  char name[NAME_SIZE];
  char pass[PASS_SIZE];
} User;

void vuln() {
  User user = {0};
  char buffer[0x400];
  bool logged_in = false;

  while (true) {
    if (logged_in) {
      printf("Hello %s!\n", user.name);

      int choice;
      while (scanf("%d", &choice) != 1) {
        printf("Try again.\n");
        while (getchar() != '\n')
          ;
      }
      getchar();

      switch (choice) {
      case 1: {
        printf("New name: ");
        fgets(user.name, strlen(user.name) + 1, stdin);
        break;
      }
      case 2: {
        printf("Here is your password: %s\n", user.pass);
        printf("New password: ");
        fgets(user.pass, strlen(user.pass) + 1, stdin);
        break;
      }
      case 3: {
        printf("See you next time %s!\n", user.name);
        return;
      }
      }
    } else {
      printf("Enter your login information: ");
      fgets(buffer, sizeof(buffer), stdin);

      char *p;
      if ((p = strchr(buffer, '\n'))) {
        *p = 0;
      }

      p = strchr(buffer, ':');
      if (p == NULL) {
        printf("Invalid login.\n");
        continue;
      }

      *p = 0;
      char *name = buffer;
      char *pass = p + 1;

      int overflow;
      overflow = strlen(pass) - PASS_SIZE;
      if (overflow >= 0) {
        printf("Too long.\n");
        continue;
      }

      overflow = strlen(name) - NAME_SIZE;
      if (overflow >= 0) {
        printf("Too long..\n");
        continue;
      }

      strcpy(user.name, name);
      strcpy(user.pass, pass);
      logged_in = true;
    }
  }
}

int main() {
  setbuf(stdout, NULL);
  vuln();
}