/*
 * Copyright (C) 2020, Matthias Weckbecker <matthias@weckbecker.name>
 *
 * License: GNU GPL, version 2 or later.
 *   See the COPYING file in the top-level directory.
 */
#include <inttypes.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <qemu-plugin.h>
#include <stdbool.h>
#include <sys/syscall.h>

QEMU_PLUGIN_EXPORT int qemu_plugin_version = QEMU_PLUGIN_VERSION;

bool activated = false;

static void vcpu_syscall(qemu_plugin_id_t id, unsigned int vcpu_index,
                         int64_t num, uint64_t a1, uint64_t a2,
                         uint64_t a3, uint64_t a4, uint64_t a5,
                         uint64_t a6, uint64_t a7, uint64_t a8)
{
  if (activated) {
    if (num != SYS_read && num != SYS_write && num != SYS_mmap && num != SYS_exit && num != SYS_exit_group) {
      printf("[-] INVALID SYSCALL: %ld\n", num);
      fflush(stdout);
      exit(1);
    }
  }
  if (!activated && num == 0x6969) {
    activated = true;
    printf("[+] FILTER ACTIVATED\n");
  }
}

QEMU_PLUGIN_EXPORT int qemu_plugin_install(qemu_plugin_id_t id,
                                           const qemu_info_t *info,
                                           int argc, char **argv)
{
  qemu_plugin_register_vcpu_syscall_cb(id, vcpu_syscall);
  return 0;
}