from pwn.red/jail

copy --from=ubuntu:25.10 / /srv
copy chal /srv/app/run
copy flag /srv/app/flag

env JAIL_TIME=0