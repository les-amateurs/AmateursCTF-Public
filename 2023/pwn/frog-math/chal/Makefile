CC=g++
CFLAGS=-masm=intel
BUILD=buildpack-deps@sha256:8f28bd087741849791b564aea220968c88f2cace4063336681cd238858e05a79
RUNNER=ubuntu@sha256:b060fffe8e1561c9c3e6dea6db487b900100fc26830b9ea2ec966c151ab4c020

.PHONY: clean run build

chal: chal.cpp
	docker run -v "$(CURDIR):/app" -w /app -it --rm $(BUILD) $(CC) chal.cpp $(CFLAGS) -o chal

build: chal

clean:
	rm chal

run: build
	docker run -v "$(CURDIR):/app" -w /app -it --rm $(RUNNER) ./chal