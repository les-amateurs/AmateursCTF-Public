FROM pwn.red/jail

COPY --from=ubuntu:22.04 / /srv
COPY chal /srv/app/run
COPY lib /srv/app/lib/
COPY flag.txt /srv/app/