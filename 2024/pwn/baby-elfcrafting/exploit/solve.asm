base equ 0x200000
ehdrsz equ 0x40
phdrsz equ 0x38

header:
    .ident: db 0x7f, "ELF"
    .class: db 0x02
    .data: db 0x01
    .ver: db 0x01
    .osabi: db 0x00
    .abiversion: db 0x00
    .pad: times 7 db 0

    .type: dw 0x02
    .machine: dw 0x3e
    .version: dd 1
    .entry: dq base
    .phoff: dq 0x40
    .shoff: dq 0
    .flags: dd 0
    .ehsize: dw ehdrsz
    .phentsize: dw phdrsz
    .phnum: dw 3
    .shentsize: dw 0x40
    .shnum: dw 0
    .shstrndx: dw 0

self:
    .type: dd 0x06
    .flags: dd 4
    .offset: dq self
    .vaddr: dq base + self
    .paddr: dq 0
    .filesz: dq phdrsz * 3
    .memsz: dq phdrsz * 3
    .align: dq 0

load:
    .type: dd 0x01
    .flags: dd 6
    .offset: dq 0
    .vaddr: dq base
    .paddr: dq 0
    .filesz: dq ehdrsz + phdrsz * 3
    .memsz: dq ehdrsz + phdrsz * 3
    .align: dq 0

interp:
    .type: dd 0x03
    .flags: dd 4
    .offset: dq linker
    .vaddr: dq base + interp
    .paddr: dq 0
    .filesz: dq linker_len
    .memsz: dq linker_len
    .align: dq 0

linker:
    db "/bin/sh", 0
linker_len equ $ - linker