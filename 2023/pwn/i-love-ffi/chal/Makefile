CC=gcc
CFLAGS=
BUILD=cargo
RUNNER=ubuntu@sha256:b060fffe8e1561c9c3e6dea6db487b900100fc26830b9ea2ec966c151ab4c020

.PHONY: clean run build

chal libi_love_ffi.so: chal.c src/lib.rs
	docker build ./cargo -t cargo
	docker run -v "$(CURDIR):/app" -w /app -it --rm $(BUILD) /bin/sh -c "cargo build --release; cp target/release/libi_love_ffi.so /lib/x86_64-linux-gnu; cp target/release/libi_love_ffi.so .; gcc chal.c -o chal -li_love_ffi -Wl,-rpath=."

build: chal

clean:
	rm chal

run: build
	docker run -v "$(CURDIR):/app" -w /app -it --rm $(RUNNER) ./chal