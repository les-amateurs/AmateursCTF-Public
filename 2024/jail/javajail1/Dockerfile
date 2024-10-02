FROM python:3.12-slim as base

RUN apt update && apt install -y openjdk-17-jre-headless

WORKDIR /app

COPY ./flag.txt /app/flag.txt
COPY ./main.py /app/run

RUN chmod +x /app/run

FROM pwn.red/jail:latest

COPY --from=base / /srv

ENV JAIL_MEM=128M JAIL_TMP_SIZE=10M JAIL_PIDS=256