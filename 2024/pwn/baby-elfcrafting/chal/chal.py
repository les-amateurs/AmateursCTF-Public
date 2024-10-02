#!/usr/local/bin/python3

from elf import *
from base64 import b64decode

def errx(exitcode: int, msg: str):
    print(msg)
    exit(exitcode)

data = b64decode(input("Give me an elf file: "))
elf = parse(data)

if elf.header.e_type != constants.ET_EXEC:
    errx(1, "must be an executable")

interps = []
for segment in elf.segments:
    if segment.p_type == constants.PT_INTERP:
        interps.append(segment)

    if segment.p_type == constants.PT_LOAD and segment.p_flags & SegmentFlags.X != 0:
        errx(1, "no executable segments")

if len(interps) != 1:
    errx(1, "only one interp")

argv = input("argv: ").split()

elf.run(argv)