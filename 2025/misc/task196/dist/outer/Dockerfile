FROM python:3.13.5@sha256:4ea77121eab13d9e71f2783d7505f5655b25bb7b2c263e8020aae3b555dbc0b2 AS app

RUN apt-get update
RUN apt-get install -y socat netcat-traditional

WORKDIR /app
COPY ./main.py /app/main.py
RUN chmod +x /app/main.py
COPY ./flag.txt /app/flag.txt
COPY ./task196.json /app/task196.json

ENTRYPOINT socat TCP-LISTEN:5000,fork,reuseaddr,bind=0.0.0.0 EXEC:"/app/main.py"