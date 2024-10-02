from Crypto.Util.strxor import strxor
from pwn import *
import string

charset = string.ascii_letters + string.digits + "{}_\x00"

payload = []

for i in charset:
    if (offset := ord(i) % 16) == 15: # flag block would be in plain sight under the mask if this were the case.
        continue
    for j in charset:
        payload.append(i.encode().hex() + "00" * (offset) + j.encode().hex() + "00" * (14 - offset))
x = "".join(payload).encode()


flag = [0]
ct = 1
while not all(flag):
    print(ct)
    r = process(['python3', 'mask-main.py'], level='error')
    r.sendlineafter(b"> ", b"1")
    r.sendlineafter(b": ", x)
    out = bytes.fromhex(r.recvline().strip().decode())
    r.sendlineafter(b"> ", b"2")
    f = bytes.fromhex(r.recvline().strip().decode())
    r.sendlineafter(b"> ", b"3")
    mask = bytes.fromhex(r.recvline().strip().decode())
    y = strxor(mask, out)
    fl = strxor(bytes.fromhex(r.recvline().strip().decode()), f)
    if flag == [0]:
        flag = [b''] * (len(fl)//16)
    fla = []
    for i in range(len(fl)//16):
        fla.append(fl[i*16:i*16+16])
    o = 0
    for i in charset:
        if (offset := ord(i) % 16) == 15:
            continue
        for j in charset:
            re = bytes.fromhex("00" * 14 + i.encode().hex() + j.encode().hex())
            a = [strxor(strxor(y[o*16:o*16+16], _), re) for _ in fla]
            if any(all(chr(_) in charset for _ in __) for __ in a):
                for asd in range(len(flag)):
                    asdf = a[asd]
                    if all(chr(_) in charset for _ in asdf):
                        asdff = asdf.decode()
                        idx = ord(asdff[-2]) % 16
                        flag[asd] = asdff[-2] + asdff[:idx] + asdff[-1] + asdff[idx:-2]
            o += 1
    ct += 1
print("".join(flag).strip("\x00"))