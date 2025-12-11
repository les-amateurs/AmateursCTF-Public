all:
	gcc chal.c -o chal -Wl,-rpath,. -Wl,--dynamic-linker,./ld-linux-x86-64.so.2 -fstack-protector-all -pie -Wl,-z,now -lseccomp
# 	zig cc -target x86_64-linux-gnu -static -s -Os solve.c -o solve.elf
	nasm -f elf64 solve.asm -o solve.o && ld solve.o -o solve.elf