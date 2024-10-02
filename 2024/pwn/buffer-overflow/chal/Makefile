all: build

build: chal.c chal.rs
	rustc chal.rs -o lib/libchal.so -C debuginfo=none -C strip=debuginfo -C no-vectorize-slp -C no-vectorize-loops -C target-feature='-mmx,-sse' --crate-type=cdylib
	gcc chal.c -o chal -lchal -Llib -Wl,-rpath,./lib -Wl,--dynamic-linker=./lib/ld-linux-x86-64.so.2 -fno-stack-protector -no-pie