FROM pwn.red/jail

COPY --from=python:3.8-slim-bullseye / /srv
COPY ./main.py /srv/app/run
COPY ./flag.py /srv/app/flag.py
RUN chmod 755 /srv/app/run

ENV JAIL_MEM=30M
