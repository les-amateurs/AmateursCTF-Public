FROM python:3.11-slim AS app
RUN pip install --no-cache-dir pycryptodome

FROM pwn.red/jail
COPY --from=app / /srv
COPY ./decryption-as-a-service.py /srv/app/run
COPY ./flag.txt /srv/app/flag.txt
RUN chmod 755 /srv/app/run

ENV JAIL_MEM=64M JAIL_TIME=12000 JAIL_POW=15000