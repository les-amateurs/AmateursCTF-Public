all: build

build: chal.c color.h
	gcc chal.c -o chal -fstack-protector-all -Wl,-z,now -pie -Wl,-rpath,./lib -Wl,--dynamic-linker,./lib/ld-linux-x86-64.so.2