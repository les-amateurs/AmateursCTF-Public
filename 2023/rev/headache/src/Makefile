all:
	python3 codegen.py
	nasm -f elf64 -o firstpass.o firstpass.asm
	gcc startup.c firstpass.o -no-pie -o firstpass.elf
	python3 obfuscate.py
	objcopy -S secondpass.elf headache

clean:
	rm -f firstpass.o firstpass.elf firstpass.asm secondpass.elf
