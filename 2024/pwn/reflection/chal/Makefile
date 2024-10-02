.PHONY: all build

all: build

build: chal.c
	gcc chal.c -o chal -Wl,-z,lazy -fno-stack-protector -no-pie -Wl,-rpath,./lib -Wl,--dynamic-linker=./lib/ld-linux-x86-64.so.2 -ffunction-sections -fdata-sections -Wl,--gc-sections
	python3 patch.py