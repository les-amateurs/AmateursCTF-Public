#!/usr/bin/env python3

import secrets

uid = secrets.randbits(48)
open('/srv/app/data/uids.txt', 'w').write(f'{uid}\n')
open(f'/srv/app/data/passwd/{uid}.txt', 'w').write(secrets.token_hex(16))
