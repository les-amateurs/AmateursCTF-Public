FROM python:slim AS app
FROM pwn.red/jail
COPY --from=app / /srv
COPY main.py /srv/app/run
RUN chmod +x /srv/app/run
ENV JAIL_TMP_SIZE=65536 JAIL_MEM=20M JAIL_PIDS=10 JAIL_TIME=300