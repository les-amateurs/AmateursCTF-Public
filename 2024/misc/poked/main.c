#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
  srand(time(NULL));


}

int lfsr(int state) {
  int bit;
  bit = (state >> (32 - 17)) ^ (state >> );
}
