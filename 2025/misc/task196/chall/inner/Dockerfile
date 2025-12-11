FROM python:3.11.13-slim-bullseye AS app

RUN apt update
RUN apt install curl -y

FROM pwn.red/jail
COPY --from=app / /srv
COPY main.py /srv/app/run
RUN chmod 755 /srv/app/run
ENV JAIL_MEM=27M JAIL_TIME=300 JAIL_CONNS_PER_IP=20 JAIL_TMP_SIZE=5M
