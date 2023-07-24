FROM python:3.10.12-slim-bullseye as base
RUN pip3 install tqdm
RUN pip3 install qiskit

FROM pwn.red/jail 

COPY --from=base / /srv

COPY ./q-cheshires-game.py /srv/app/run
COPY ./flag.txt /srv/app/flag.txt

RUN chmod 755 /srv/app/run

ENV JAIL_TIME=180 JAIL_MEM=100M JAIL_TMP_SIZE=100M JAIL_POW=45000