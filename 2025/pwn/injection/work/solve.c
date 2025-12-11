#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main() {
  size_t status;
  int fd;

  setbuf(stdout, NULL);
  printf("hello!\n");

  fd = open("/tmp/libc.so.6", O_WRONLY);
  printf("fd = %d\n", fd);

  status = lseek(fd, 0x11a000, SEEK_SET);
  printf("status = %ld\n", status);

  char death[0x1000];
  memset(death, 0x41, sizeof(death));
  status = write(fd, death, sizeof(death));
  perror("write");
  printf("status = %ld\n", status);
  close(fd);
}