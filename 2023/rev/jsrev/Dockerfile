FROM python:3.10-slim-bullseye

RUN pip install --no-cache-dir Flask gunicorn
WORKDIR /app

COPY app.py ./main.py
COPY templates ./templates
COPY static ./static

USER 1000
EXPOSE 8080

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8080", "main:app"]