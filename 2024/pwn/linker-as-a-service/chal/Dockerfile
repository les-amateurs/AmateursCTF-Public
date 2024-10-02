FROM python:3.9 as base

FROM pwn.red/jail

COPY --from=base / /srv
COPY elf.py /srv/app/
COPY flag.txt /srv/app/
COPY chal.py /srv/app/run
COPY ld-linux-x86-64.so.2 /srv/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2

RUN chmod +x /srv/app/run

ENV JAIL_MEM=32M JAIL_TIME=9999999