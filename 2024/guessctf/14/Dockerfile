FROM python:3.10-slim-buster

RUN pip3 install flask
RUN pip3 install pycryptodome
COPY . /app

WORKDIR /app

EXPOSE 1431

ENTRYPOINT ["python3", "server.py"]