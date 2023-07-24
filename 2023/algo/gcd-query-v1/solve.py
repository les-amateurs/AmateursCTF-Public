from pwn import *
from tqdm import tqdm

io = remote('amt.rs', 31692)

# do redpwn proof of work
# req = io.readline().decode().strip("proof of work: ")
# print(f"[+] running: {req}")
# pow = subprocess.run(req, shell=True, capture_output=True).stdout

# print(f"[+] pow: {pow.decode()}")
# io.sendafter(b"solution: ", pow)

for i in tqdm(range(10)):
    payload = 2**2049
    payload = str(payload).encode()
    gcd = 1
    num = 1

    io.recvuntil(b": ")
    qc = 0
    
    while gcd != 2**2049:
        io.sendline(str(num).encode()+b" "+payload)
        gcd = int(io.recvuntil(b": ").decode().split("\n")[0])
        num += gcd
        qc += 1

    secret = 2**2050 - num

    for i in range(qc, 1412):
        io.sendline(b"1 1")
        io.recvuntil(b": ")
    io.sendline(str(secret).encode())

print(io.recvline().strip().decode())