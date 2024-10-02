.PHONY: all chal filter

all: chal filter

chal: chal.c
	gcc chal.c -o chal -fstack-protector-strong -pie -fPIE -Wl,-z,now -masm=intel

filter:
	gcc $(pkg-config --cflags --libs glib-2.0) -fPIC -shared filter.c -o libfilter.so