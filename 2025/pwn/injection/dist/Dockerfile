from ubuntu:25.10 as base

run apt-get update && \
    apt-get install -y \
    libseccomp-dev

from pwn.red/jail

copy --from=base / /srv
copy flag /flag
copy nsjail.cfg /nsjail.cfg
copy hook.sh /jail/hook.sh
copy run.sh /srv/app/run
copy chal /srv/app/chal

env JAIL_TIME=0 JAIL_PIDS=5 JAIL_MEM=200M