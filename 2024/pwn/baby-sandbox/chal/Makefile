.PHONY: all build

all: build

build: chal.c
	gcc chal.c -o chal -Wl,-rpath,./lib -Wl,--dynamic-linker=./lib/ld-linux-x86-64.so.2 -pie -fPIE -Wl,-z,now -fstack-protector-strong -masm=intel