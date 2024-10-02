FROM pwn.red/jail

COPY --from=python:3.11-slim / /srv
COPY server.py /srv/app/run
COPY flag.txt /srv/app/
RUN  chmod +x /srv/app/run

ENV JAIL_MEM=32M