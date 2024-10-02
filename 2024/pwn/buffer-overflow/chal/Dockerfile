FROM pwn.red/jail

COPY --from=ubuntu:22.04 / /srv
COPY lib /srv/app/lib/
COPY chal /srv/app/run
COPY flag.txt /srv/app/