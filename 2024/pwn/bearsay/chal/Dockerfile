FROM pwn.red/jail

COPY --from=ubuntu:22.04 / /srv
COPY lib /srv/app/lib/
COPY chal /srv/app/run
COPY flag.txt /srv/app/

ENV JAIL_TIME=60 JAIL_MEM=32M JAIL_PIDS=60