FROM python:3.10.12-slim AS app
RUN pip install --no-cache-dir pycryptodome

FROM pwn.red/jail
COPY --from=app / /srv
COPY ./faked-onion.py /srv/app/run
COPY ./flag.txt /srv/app/flag.txt
RUN chmod 755 /srv/app/run

ENV JAIL_MEM=30M JAIL_TIME=12000