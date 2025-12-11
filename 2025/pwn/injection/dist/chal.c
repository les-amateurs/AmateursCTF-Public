#define _GNU_SOURCE
#include <fcntl.h>
#include <seccomp.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <unistd.h>

#define FLAG_BYTES (0x100)

void install_seccomp() {
  scmp_filter_ctx ctx;
  ctx = seccomp_init(SCMP_ACT_KILL);
  int ret = 0;
  ret |= seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 0);
  ret |= seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(read), 0);
  ret |= seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(open), 0);
  ret |= seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(execve), 0);
  ret |= seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit), 0);
  ret |= seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit_group), 0);
  ret |= seccomp_load(ctx);
  if (ret) {
    printf("seccomp failed");
    exit(1);
  }
}

int main() {
  char flag[FLAG_BYTES];
  int fd;
  size_t nbytes;

  setbuf(stdout, NULL);

  fd = open("/tmp/flag", O_RDONLY);
  if (fd < 0) {
    printf("failed to open flag.\n");
    printf("contact an admin\n");
    return 1;
  }

  flag[read(fd, flag, FLAG_BYTES - 1)] = 0;
  close(fd);

  fd = open("/tmp/flag", O_WRONLY | O_TRUNC);
  dprintf(fd, "amateursCTF{fake_flag}");
  close(fd);

  printf("elf bytes: ");
  if (scanf("%ld", &nbytes) != 1)
    return 1;
  getchar();

  uint8_t *elf = malloc(nbytes);
  if (elf == NULL)
    return 1;

  printf("reading %ld bytes\n", nbytes);
  fread(elf, sizeof(uint8_t), nbytes, stdin);
  fd = open("/tmp/solve", O_WRONLY | O_CREAT, 0777);
  printf("fd = %d\n", fd);
  printf("written = %ld\n", write(fd, elf, nbytes));
  printf("done writing elf\n");
  close(fd);

  if (fork() == 0) {
    install_seccomp();
    execve("/tmp/solve", NULL, NULL);
    perror("execve");
    exit(1);
  } else {
    while (true) {
      sleep(1);
    }
  }
}