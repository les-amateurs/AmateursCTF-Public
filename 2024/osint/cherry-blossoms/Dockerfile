FROM python:3.9-slim AS app

FROM pwn.red/jail

COPY --from=app / /srv
COPY ./flag.txt ./locations.json /srv/app/
COPY ./main.py /srv/app/run
RUN chmod 755 /srv/app/run

ENV JAIL_MEM=60M JAIL_ENV_PATH=/usr/local/bin JAIL_TIME=90 JAIL_POW=15000