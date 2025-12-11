#!/usr/local/bin/python3
import warnings
warnings.filterwarnings("ignore")
prog = bytes.fromhex(input('')).decode()
for _ in range(int(input())):
    tc_inp = __import__('json').loads(bytes.fromhex(input('')).decode())
    exec(prog)
    print(__import__('json').dumps(p(tc_inp)))

