FROM pwn.red/jail

COPY --from=python:3.10.12-slim / /srv
COPY ./main.py /srv/app/run
COPY ./flag.py /srv/app/flag.py
RUN chmod 755 /srv/app/run

ENV JAIL_MEM=30M JAIL_TIME=1200