#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define NOTES (0x10)
#define NOTE_SIZE (0x67)

char checkbuf[NOTE_SIZE];
void check() {
  printf("check.\n");
  if (strcmp(checkbuf, "ALL HAIL OUR LORD AND SAVIOR TEEMO") == 0) {
    system("sh");
  }
}

int rep = 1;
int main() {
  setbuf(stdout, NULL);

  char *notes[NOTES];
  while (true) {
    unsigned int choice;
    unsigned int idx;

    for (int i = 0; i < rep; i++) {
      printf("67\n");
    }
    rep++;

    printf("> ");
    scanf("%u", &choice);
    getchar();

    if (choice == 67) {
      check();
    }
    if (choice >= 4) {
      continue;
    }

    printf("> ");
    scanf("%u", &idx);
    getchar();
    if (idx >= NOTES) {
      printf("bad index.\n");
      continue;
    }

    switch (choice) {
    case 0: {
      notes[idx] = malloc(NOTE_SIZE);
      break;
    }
    case 1: {
      free(notes[idx]);
      break;
    }
    case 2: {
      printf("data> ");
      read(0, notes[idx], NOTE_SIZE);
      break;
    }
    case 3: {
      printf("data> ");
      write(1, notes[idx], NOTE_SIZE);
      printf("\n");
      break;
    }
    }
  }
}