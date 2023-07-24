CC=gcc
CFLAGS=-fno-stack-protector -lseccomp
BUILD=seccomp
RUNNER=ubuntu@sha256:b060fffe8e1561c9c3e6dea6db487b900100fc26830b9ea2ec966c151ab4c020

.PHONY: clean run build

chal: chal.c
	docker build ./seccomp -t seccomp
	docker run -v "$(CURDIR):/app" -w /app -it --rm $(BUILD) $(CC) chal.c $(CFLAGS) -o chal

build: chal

clean:
	rm chal

run: build
	docker run -v "$(CURDIR):/app" -w /app -it --rm $(RUNNER) ./chal