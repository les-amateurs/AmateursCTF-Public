#!/usr/bin/python3

from capstone import *
from capstone.x86 import X86Op, X86_OP_IMM
import os

ALLOWED_MNEMONICS = ["jmp", "add", "mov", "sub", "inc", "dec", "cmp", "push", "pop", "int3"]

shellcode = b"\xbc\x00\x70\x76\x06" + bytes.fromhex(input("shellcode: ")) + b"\xcc"
if len(shellcode) > 0x1000:
    exit("too long")

cs = Cs(CS_ARCH_X86, CS_MODE_32)
cs.detail = True
it = cs.disasm(shellcode, 0x1337000)

offsets = []
nbytes = 0
insns = list(it)

for insn in insns:
    print(f"{insn.address:04x} {insn.mnemonic} {insn.op_str}")
    if not any(part in insn.mnemonic for part in ALLOWED_MNEMONICS):
        exit("bad insn")
    offsets.append(insn.address)
    nbytes += len(insn.bytes)

if nbytes != len(shellcode):
    exit("error decoding all the instructions")

for insn in insns:
    if "jmp" in insn.mnemonic:
        if len(insn.operands) < 1:
            exit("bad")

        target = insn.operands[-1]
        assert type(target) == X86Op

        if target.type != X86_OP_IMM:
            exit("jmp must be imm")
        
        addr = target.imm
        if addr not in offsets:
            exit("jmp must be valid")

template = bytearray(open("template.elf", "rb").read())
template[0x2000:0x3000] = shellcode.ljust(0x1000, b"\xcc")
with open("/tmp/solve.elf", "wb+") as fp:
    fp.write(template)
os.chmod("/tmp/solve.elf", 0o777)
os.execl("/tmp/solve.elf", "/tmp/solve.elf")