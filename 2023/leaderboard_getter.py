#!/usr/bin/env python3

# taken from https://gist.githubusercontent.com/captainGeech42/c68ed2afcc6818c82d394487a33f5eef/raw/ccb712a890b611b355602ae53b76e60d8856997c/export_ctftime.py

import requests
import sys

# use an account with bit 1<<2 set (put 7 for ultimate laziness)

BASE_URL = "https://ctf.amateurs.team"
TEAM_TOKEN = "REDACTED" # the thing from the url on the team profile page

r = requests.post(BASE_URL + "/api/v1/auth/login", json={"teamToken": TEAM_TOKEN})
if r.status_code != 200 or r.json()["kind"] != "goodLogin":
    print("Failed to authenticate to rCTF, bad team token?")
    sys.exit(1)

auth_token = r.json()["data"]["authToken"]
print("authed")

r = requests.get(BASE_URL + "/api/v1/integrations/ctftime/leaderboard", headers={"Authorization": f"Bearer {auth_token}"})

if r.status_code != 200:
    print("couldn't get scoreboard")
    print(r.content.decode())

with open("ctftime.json", "w") as f:
    f.write(r.content.decode())

print("exported scoreboard to ctftime.json")