code = open("code.jvm", "rb").read()

segments = code.split(b'5')[1:] # 5 is pop

flag = ''
for s in segments:
    print(s, len(s))
    if len(s) < 10:
        flag = chr(s[3]) + flag
    elif len(s) == 10:
        offset = s[3]
        flag = chr(s[6] + offset) + flag
    else:
        flag = 'A' + flag
print(flag)