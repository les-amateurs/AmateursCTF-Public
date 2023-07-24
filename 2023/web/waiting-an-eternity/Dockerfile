FROM python:3.10-slim-bullseye

RUN pip install --no-cache-dir Flask gunicorn

COPY main.py /

USER 1000

EXPOSE 8080

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8080", "main:app"]