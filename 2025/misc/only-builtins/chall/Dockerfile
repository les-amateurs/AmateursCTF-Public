FROM python@sha256:4d440b214e447deddc0a94de23a3d97d28dfafdf125a8b4bb8073381510c9ee2

RUN apt-get update && apt-get install gcc socat --yes

COPY --chown=root:root flag.txt /flag.txt
COPY --chown=root:root chal.py /srv/app/run
RUN mkdir /tmp/work && \
    chmod 0733 /tmp/work && \
    chmod 0755 /srv/app/run /flag.txt

WORKDIR /srv/app
USER nobody

CMD ["socat", "TCP-LISTEN:5000,fork,reuseaddr,bind=0.0.0.0", "EXEC:/srv/app/run"]