FROM pwn.red/jail

COPY --from=python:3.11-slim / /srv
COPY main.py /srv/app/run
COPY flag.txt /srv/app/

RUN  chmod +x /srv/app/run

ENV JAIL_MEM=32M
ENV JAIL_TMP_SIZE=10M