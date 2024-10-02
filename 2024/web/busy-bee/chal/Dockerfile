FROM busybox:1.35

RUN adduser -D static
USER static
WORKDIR /home/static

COPY . .

CMD ["busybox", "httpd", "-f", "-v", "-p", "3000"]
