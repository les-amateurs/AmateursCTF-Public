FROM pwn.red/jail

COPY --from=python:3.11-slim / /srv
COPY chal.py  /srv/app/run
COPY elf.py   /srv/app/elf.py
COPY flag.txt /srv/app/flag.txt
COPY hook.sh  /jail/

ENV JAIL_MEM=32M