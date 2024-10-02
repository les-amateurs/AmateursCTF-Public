.PHONY: all build

all: build

build:
	gcc chal.c -o chal -fPIC -pie -Wl,-z,now -fstack-protector-all -Wl,-rpath,./lib -Wl,--dynamic-linker=./lib/ld-linux-x86-64.so.2