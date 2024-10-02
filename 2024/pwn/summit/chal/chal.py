#!/usr/local/bin/python3

from elf import *
from base64 import b64decode

data = b64decode(input("Give me an elf file: "))

if len(data) > 73:
    print("you know this is a golfing challenge right?")
    exit(1)

elf = parse(data)
elf.run()