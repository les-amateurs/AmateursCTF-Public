import sys
import secret
from pwn import *

def input():
    return p.recvline().strip().decode()

p = remote(args.HOST or "localhost", args.PORT or "5000")

for _ in range(int(input())):
    ans = secret.solve(list(map(int, input().split())))
    ans = map(str, ans)
    ans = " ".join(ans)
    p.sendline(ans)

print(input(), file=sys.stderr)
