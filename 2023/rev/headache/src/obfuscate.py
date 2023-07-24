from lief import *
from pwn import u32, p32

# thank you unvariant
file = parse("firstpass.elf")

text_section = file.get_section(".text")
code = bytes(text_section.content)
code = [u32(code[i:i+4]) for i in range(0, len(code), 4)]

xors = []
adjust = text_section.virtual_address

for symbol in file.symbols:
    if "encoded" in symbol.name and "end" not in symbol.name:
        xor = int(symbol.name.split("_")[1])
        start = (symbol.value - adjust) // 4
        end = (file.get_symbol(symbol.name + "_end").value - adjust) // 4
        xors.append((start, end, xor))

for start, end, xor in reversed(sorted(xors)):
    for i in range(start, end):
        code[i] ^= xor

text_section.content = list(b"".join([p32(n) for n in code]))
text_section.segments[0].add(ELF.SEGMENT_FLAGS.W)

file.write("secondpass.elf")