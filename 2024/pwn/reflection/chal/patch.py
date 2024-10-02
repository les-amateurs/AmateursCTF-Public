from elf import *
from capstone import *

elf = parse(open("chal", "rb").read())

text = elf.section(".text")
content = elf.content(text)

ranges = [(0x4010f0, 0x20), (0x401120, 6), (0x4010b0, 50), (0x401080, 0x20), (0x401070, 4)]
for start, length in ranges:
    offset = start - text.sh_addr
    content[offset:offset+length] = b"\xc3" * length

cs = Cs(CS_ARCH_X86, CS_MODE_64)
locs = [0x0401066, 0x0401075, 0x04010a1, 0x04010e2, 0x04010e9, 0x0401111]
for loc in locs:
    loc -= text.sh_addr
    instrs = cs.disasm(content[loc:loc+0x20], 0)
    try:
        while insn := next(instrs):
            if "nop" in insn.mnemonic:
                length = len(insn.bytes)
                content[loc+insn.address:loc+insn.address+length] = b"\xc3" * length
    except StopIteration:
        pass

content = elf.content(elf.section(".fini"))
content[:] = b"\xc3" * len(content)
content = elf.content(elf.section(".init"))
content[:] = b"\xc3" * len(content)

elf.write("chal")

