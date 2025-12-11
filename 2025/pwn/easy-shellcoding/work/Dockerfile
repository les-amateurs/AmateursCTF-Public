from ubuntu:25.10 as base
run apt-get update && \
    apt-get install -y \
        python3 python3-pip
run pip3 install capstone --break

from pwn.red/jail
copy --from=base / /srv
copy chal.py /srv/app/run
copy template.elf /srv/app/
copy flag /srv/app/

env JAIL_TIME=0 JAIL_POW=10 JAIL_MEM=100M JAIL_TMP_SIZE=1M