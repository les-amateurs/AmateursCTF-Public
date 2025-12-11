#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define MAX_NOTES (0x10)
char *notes[MAX_NOTES];

int main() {
  setbuf(stdout, NULL);

  puts("CrAzY fSOP");
  puts("1. create note");
  puts("2. delete note");
  puts("3. view note");

  while (true) {
    int choice;
    int idx;

    printf("which operation: ");
    if (scanf("%d", &choice) != 1)
      goto done;
    getchar();

    printf("which note: ");
    if (scanf("%d", &idx) != 1)
      goto done;
    getchar();

    switch (choice) {
    case 1: {
      size_t size;
      printf("size: ");
      if (scanf("%lx", &size) != 1)
        goto done;
      getchar();

      char *buf = malloc(size);
      printf("data: ");
      read(STDIN_FILENO, buf, size);
      notes[idx] = buf;
      break;
    }
    case 2: {
      free(notes[idx]);
      notes[idx] = 0;
      break;
    }
    case 3: {
      printf("data: %s\n", notes[idx]);
      break;
    }
    default: {
      goto done;
    }
    }
  }

done:
  puts("goodbye...");
}