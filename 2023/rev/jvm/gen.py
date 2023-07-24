import random

GOOD = 27
BAD = 37
def match_char_exact(c):
    # generate code to check if top of stack matches c
    # 8 bytes
    reg = 0
    return [
        53, reg, # pop TOS to reg
        12, reg, ord(c), # subtract c from reg
        42, reg, BAD, # if reg != 0, jump to BAD
    ]

def match_char_offset(c, offset):
    # generate code to check if top of stack matches c with offset obfuscation
    # 11 bytes
    reg = random.randint(0, 3) # pick a random register
    return [
        53, reg, # pop TOS to reg
        12, reg, offset, # add offset to reg
        12, reg, ord(c) - offset, # subtract c from reg
        42, reg, BAD, # if reg != 0, jump to BAD
    ]

offset_table = {}
flag = "amateursCTF{wh4t_d0_yoU_m34n_j4v4_isnt_A_vm?}"
print(len(flag))
for c in flag:
    if c not in offset_table:
        offset_table[c] = random.randint(0, ord(c) // 2)

def match_str(s):
    code = []
    for c in s[::-1]:
        code += match_char_offset(c, offset_table[c])
    return code

def match_str_exact(s):
    code = []
    for c in s[::-1]:
        code += match_char_exact(c)
    return code

with open("code.jvm", "wb") as f:
    code = bytes([
        # load '> ' on stack
        54, b' '[0],                    # 0
        54, b'>'[0],                    # 2
        34, 34,                         # 4
        # load 42 in A but in trolly way
        8, 0, 10,
        9, 0, 0,
        9, 0, 0,
        8, 0, 5,
        # read to stack
        32,                             # 18
        # subtract 1 from A
        12, 0, 1,                       # 19
        # if A != 0, jump to read
        42, 0, 18,                       # 22 
        # jump past end statements
        43, 44,                         # 25
        54, b'S'[0], # good             # 27
        54, b'E'[0],                    # 29
        54, b'Y'[0],                    # 31
        34, 34, 34, 127,               # 33   
        54, b'O'[0], # bad              # 37
        54, b'N'[0],                    # 39
        34, 34, 127,                   # 41
        # 44 START OF LOGIC
        *match_char_exact('}'),         # 44
        *match_char_offset('?', 9),     # 52
        *match_char_offset('m', 10),     # 63
        *match_char_offset('v', 21),     # 74
        *match_char_exact('_'),         # 85
        53, 0,                          # 93
        8, 1, 1,                        # 95
        0, 1,                           # 98
        9, 1, 1,                        # 100
        8, 2, 7,                        # 103
        # while C != 0
        9, 0, 0,                        # 106
        12, 2, 1,                       # 109
        42, 2, 106, # double A 7 times  # 112
        8, 0, 2,                        # 115
        13, 0, 1,                       # 118
        13, 1, 1,                       # 121
        42, 0, BAD,                      # 124 
        *match_char_exact('_'),        # 127
        *match_char_offset('t', 1),     # 135
        *match_char_offset('n', 3),     # 146
        *match_char_offset('s', 3),     # 157
        *match_char_offset('i', 7),     # 168
        *match_char_exact('_'),        # 179
        # idgaf about PC at this point, since bytes cant store that high so we cant jump lol
        *match_str('j4v4'),
        *match_char_exact('_'),
        *match_str('m34n'),
        *match_char_exact('_'),
        *match_str('yoU'),
        *match_char_exact('_'),
        *match_str('d0'),
        *match_char_exact('_'),
        *match_str('wh4t'),
        *match_str_exact('amateursCTF{'),
        # jmp to good
        43, GOOD,                       
    ])
    print(len(code))
    f.write(code)
