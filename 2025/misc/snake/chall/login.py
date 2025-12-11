#!/usr/bin/env python3

import sys

uid = sys.argv[1]
password = sys.argv[2]
is_admin = False

with open('/srv/app/data/uids.txt') as f:
    uids = f.read().splitlines()
    if uid not in uids:
        sys.exit(1)

    if uid == uids[0]:
        is_admin = True

with open(f'/srv/app/data/passwd/{uid}.txt') as f:
    stored_password = f.read().strip()
    if password != stored_password:
        sys.exit(1)

if is_admin:
    sys.exit(255)
else:
    sys.exit(0)
