FROM busybox:1.35

RUN adduser -D static
USER static
WORKDIR /home/static

COPY agile-rut.otf index.html ./

CMD ["busybox", "httpd", "-f", "-v", "-p", "3000"]
