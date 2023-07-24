
with open('fleg', 'r') as f:
    flag = bytes.fromhex(f.read())
    realflag = ""
    for i in range(len(flag)//2):
        realflag += chr(flag[i*2])
        realflag += chr(flag[i*2] ^ flag[i*2+1])
    print(realflag)