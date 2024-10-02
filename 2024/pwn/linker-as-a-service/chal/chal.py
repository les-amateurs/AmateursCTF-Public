#!/usr/bin/python3

from elf import *
from base64 import b64decode

data = b64decode(input("Give me an elf file: "))
elf = parse(data)

if elf.header.e_type != constants.ET_DYN:
    print("go away")
    exit(1)

relocs = elf.dyntag(constants.DT_RELA).d_un.d_val

interps = []
for segment in elf.segments:        
    if segment.p_type == constants.PT_INTERP:
        interps.append(segment)

    if (segment.p_vaddr & ~0xfff) <= relocs and relocs <= ((segment.p_vaddr + segment.p_memsz + 0xfff) & ~0xfff) and (segment.p_flags & SegmentFlags.W) != 0:
        print("no")
        exit(1)

if len(interps) != 1:
    print("nuh uh")
    exit(1)
interp = interps[0]

if elf.content(interp) != b"/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2\x00":
    print("hmmmmm")
    exit(1)

elf.run(env={
    "LD_TRACE_LOADED_OBJECTS": "1",
    "LD_WARN": "yes",
})