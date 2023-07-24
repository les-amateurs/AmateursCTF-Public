import random
import time
import sympy
from randcrack import RandCrack
from Crypto.Util.number import *
from pwn import *
from Crypto.Cipher import AES

def pad():
    while len(x := bin(rc.predict_getrandbits(32))[2:]) == 32:
        pass
    x = "0" * (32 - len(x)) + x
    return int(x[:14], 2)

def crackrandom():
    for i in range(156):
        z = True
        while z:
            try:
                io.recvuntil(b"Enter Arguments: ")
                io.sendline(b"128")
                y = int(io.recvline().decode())
                z = False
            except:
                pass
        x = y-1
        x = bin(x)[2:]
        for j in range(4):
            rc.submit(int(x[-32:], 2))
            try:
                x = x[:-32]
            except:
                pass
    return True

timetime = time.time()
real = False
counter = 0
while not real:
    counter += 1
    try:
        io = remote('amt.rs', 31311)
        rc = RandCrack()
        counts = []
        if crackrandom():
            for i in range(3):
                count = 0
                while pad() != 0:
                    count += 1
                counts.append(str(count).encode())
        else:
            print("failed")
        
        for i in counts:
            io.recvuntil(b"Enter Arguments: ")
            io.sendline(b"a" + i)
            io.recvuntil(b"Enter Arguments: ")
            io.sendline(b"draw")
            assert b"Success!" in io.recvline(), "unlucky"
        io.recvline()
        io.recvuntil(b"Enter Arguments: ")
        io.sendline(b"flag")
        
        enc = io.recvline().strip().decode()
        
        iv = b"\x00" * 16
        key = b"\x00" * 16
        
        aescbc = AES.new(key, AES.MODE_CBC, iv=iv)
        flag = aescbc.decrypt(bytes.fromhex(enc))
        
        assert flag[-1] == b"}"[0], "bad key"
        
        print((b"a" + flag[16:]).decode())
        real = True
    except Exception as e:
        print(e)
        io.close()
io.close()
print(f"{time.time() - timetime} seconds\n{counter} attempts")