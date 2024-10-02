FROM pwn.red/jail

COPY --from=ubuntu:22.04 / /srv
COPY flag.txt /srv/app/
COPY lib /srv/app/lib/
COPY chal /srv/app/run