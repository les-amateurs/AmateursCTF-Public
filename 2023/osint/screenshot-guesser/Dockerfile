FROM python:3.9-slim AS app

FROM pwn.red/jail

COPY --from=app / /srv
COPY ./flag.txt ./locations.json ./bear.bin /srv/app/
COPY ./main.py /srv/app/run
COPY ./bear.bin /srv/bear.bin
RUN chmod 755 /srv/app/run

ENV JAIL_MEM=30M JAIL_ENV_PATH=/usr/local/bin JAIL_TIME=120 JAIL_POW=15000
