#include <stdio.h>
#include <stdlib.h>

void win() { system("sh"); }

int main() {
  char buf[0x100];
  size_t size;

  setbuf(stdout, NULL);

  printf("how much would you like to write? ");
  scanf("%ld", &size);
  getchar();
  fgets(buf, size, stdin);
}