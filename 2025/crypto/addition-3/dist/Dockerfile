FROM python:slim AS app
COPY chall.py /srv/app/run
RUN chmod +x /srv/app/run
COPY flag.txt /srv/app/
RUN apt-get update
RUN apt-get install -y socat
RUN pip install --no-cache-dir pycryptodome
WORKDIR /srv/app
ENTRYPOINT socat TCP-LISTEN:5000,fork,reuseaddr,bind=0.0.0.0 EXEC:"/srv/app/run"