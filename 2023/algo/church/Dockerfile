FROM pwn.red/jail

COPY --from=ubuntu:22.04 / /srv

COPY church /srv/app/run

ENV JAIL_TIME=60 JAIL_MEM=50M
