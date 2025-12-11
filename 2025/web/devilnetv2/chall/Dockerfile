FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y chromium chromium-driver && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER=/usr/bin/chromedriver

RUN pip install selenium

COPY app.py .
COPY web.py .

# create a new user to run the app
RUN groupadd -r teemo \
    && useradd -r -g teemo teemo \
    && mkdir -p /home/teemo/ \
    && chown -R teemo:teemo /home/teemo

USER teemo
EXPOSE 9192

ENTRYPOINT ["python3", "app.py"]