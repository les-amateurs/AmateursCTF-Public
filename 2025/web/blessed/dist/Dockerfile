FROM python:3.12-slim

WORKDIR /app

RUN pip install playwright flask

RUN playwright install --with-deps chromium

COPY main.py .

EXPOSE 8888

ENTRYPOINT ["python3", "main.py"]