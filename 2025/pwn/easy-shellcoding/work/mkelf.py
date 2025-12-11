from pwnc.minelf import *
from pwn import u32
from ctypes import sizeof

CODE_BASE = 0x1337000
STACK_SIZE = 0x1000
STACK_BASE = 0x6767000 - STACK_SIZE

elf = ELF(bits=32, little_endian=True, raw_elf_bytes=b"\0" * 0x3000)
elf.header.ident.magic.raw = u32(b"\x7fELF")
elf.header.ident.bits = 1
elf.header.ident.endianness = 1
elf.header.type = 2
elf.header.machine = 0x03
elf.header.entrypoint = CODE_BASE
elf.header.segment_offset = sizeof(elf.Header)
elf.header.sizeof_header = sizeof(elf.Header)
elf.header.sizeof_segment = sizeof(elf.Segment)
elf.header.number_of_segments = 4

elf.segments[1].type = 0x6474e551
elf.segments[1].flags = elf.Segment.Flags.R | elf.Segment.Flags.W
elf.segments[2].type = elf.Segment.Type.LOAD
elf.segments[2].virtual_address = CODE_BASE
elf.segments[2].flags = elf.Segment.Flags.R | elf.Segment.Flags.X
elf.segments[2].offset = 0x2000
elf.segments[2].file_size = 0x1000
elf.segments[2].mem_size = 0x1000
elf.segments[3].type = elf.Segment.Type.LOAD
elf.segments[3].virtual_address = STACK_BASE
elf.segments[3].flag = elf.Segment.Flags.R | elf.Segment.Flags.W
elf.segments[3].file_size = 0
elf.segments[3].mem_size = STACK_SIZE

with open("template.elf", "wb+") as fp:
    fp.write(elf.raw_elf_bytes)