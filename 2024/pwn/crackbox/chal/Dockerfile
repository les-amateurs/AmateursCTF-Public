FROM ubuntu:24.04 as base

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update --fix-missing
RUN apt-get install -y \
    libcapstone-dev \
    libdw-dev \
    libnuma-dev \
    liburing-dev \
    libglib2.0-dev

FROM pwn.red/jail

COPY --from=base / /srv
COPY chal /srv/app/
COPY libfilter.so /srv/app/
COPY qemu-x86_64 /srv/app/qemu
COPY flag.txt /srv/app/
COPY run.sh /srv/app/run

RUN chmod +x /srv/app/run

ENV JAIL_MEM=32M JAIL_TIME=60