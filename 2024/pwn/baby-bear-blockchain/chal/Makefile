BUILD=baby-bear-blockchain-build
GCC=docker run --rm -w /build -v "$(PWD)":/build -it $(BUILD) gcc

.PHONY: all build gcc

all: build

gcc: build.dockerfile
	docker build -f build.dockerfile . -t $(BUILD)

build: gcc
	$(GCC) chal.c -lseccomp -o chal -O1 -Wno-unused-result -fstack-protector-all -Wl,-z,now -pie -ffunction-sections -fdata-sections -flto -Wl,-rpath,./lib -Wl,--dynamic-linker=./lib/ld-linux-x86-64.so.2 -g

# firedancer commit 36ba4fe295338c8721a1660366d722b1ec52b75c