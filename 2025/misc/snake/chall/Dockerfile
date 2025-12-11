FROM alpine:latest

RUN apk add --no-cache bash python3 py3-pip socat && \
    adduser -D -u 1000 user && \
    mkdir -p /srv/app/data/passwd /srv/app/data/score && \
    chmod 777 /srv/app/data /srv/app/data/passwd /srv/app/data/score

COPY --chown=root:root readflag /readflag
COPY --chown=root:root flag.txt /flag.txt
COPY --chown=root:root make_admin.py login.py snake.sh run /srv/app/
RUN chmod 0755 /srv/app/make_admin.py /srv/app/login.py /srv/app/snake.sh /srv/app/run && \
    chmod 4755 /readflag && \
    chmod 0400 /flag.txt

WORKDIR /srv/app
USER user

CMD ["/srv/app/run"]
