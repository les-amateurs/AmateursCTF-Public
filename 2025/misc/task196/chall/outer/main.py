#!/usr/local/bin/python3
import json
from random import shuffle
import subprocess

p = subprocess.Popen(['nc', 'inner', '5000'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
with open('task196.json', 'r') as f:
    testcases = [*enumerate(json.load(f))]

shuffle(testcases)
tc_inp = b'\n'.join([json.dumps(tc[1]['input']).encode().hex().encode() for tc in testcases])
tc_out = b'\n'.join([json.dumps(tc[1]['output']).encode() for tc in testcases]) + b'\n'

inp = input('task196 sol (hex) > ')

res = p.communicate(inp.encode() + b'\n' + str(len(testcases)).encode() + b'\n' + tc_inp + b'\n')[0].split(b'\n')
for i2, (i, tc) in enumerate(testcases):
    try:
        res2 = json.loads(res[i2])
    except Exception as e:
        res2 = "(ERROR)"
    if tc['output'] != res2:
        print(f'fail on tc {i}')
        print('=== EXPECTED ===')
        print(tc['output'])
        print('=== ACTUAL ===')
        print(repr(res2))
        exit()

if len(inp) > 198:
    print('your code works but it does not beat my score!!!')
    exit()

with open('flag.txt', 'r') as f:
    print('u win', f.read())

