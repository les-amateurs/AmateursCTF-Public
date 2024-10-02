FROM pwn.red/jail

COPY --from=busybox:musl / /srv

COPY run.sh /srv/app/run
COPY chal.py /srv/app/
COPY elf.py /srv/app/
COPY flag.txt /srv/app/
COPY python-static.tar.xz /srv/app/
RUN  cd /srv/app && tar -xvf python-static.tar.xz
RUN  chmod +x /srv/app/run

ENV JAIL_MEM=32M