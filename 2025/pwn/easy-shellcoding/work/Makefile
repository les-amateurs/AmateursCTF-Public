all:
	nasm -f bin solve.asm -o solve.bin
	nasm -f elf32 solve.asm -o solve.o && ld solve.o -o solve.elf -m elf_i386