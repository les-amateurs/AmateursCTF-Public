import os

plants = {".":"g0", "0":"$0", " ": ";3", "*":"^0"}
START = """
.......
.......
.......
...*...
... ...
... ...
... ...
""".strip()
START_0 = """
.......
.......
.......
...0...
... ...
... ...
... ...
""".strip()
START_EMPTY = """
.......
.......
.......
... ...
... ...
... ...
... ...
""".strip()
AND = """
. ... .
. .0. .
.. . ..
... ...
..0. ..
.... ..
... ...
""".strip()
OR = """
. ... .
.. . ..
... ...
..0. ..
... ...
... ...
... ...
""".strip()
CROSS = """
. ... .
. ... .
.. . ..
. . . .
.. . ..
. ... .
. ... .
""".strip()
XOR = """
. ... .
.. . ..
... ...
... ...
... ...
... ...
... ...
""".strip()
NOT = """
... ...
... ...
... ...
..0 ...
... ...
... ...
""".strip()
TURN = """
. . . .
 . . . 
. ... .
 ..... 
.......
.......
.......
""".strip()
TURN2_L = """
.......
.......
 ......
. .....
 . ....
. . ...
.. . ..
""".strip()
TURN2_R = "\n".join(i[::-1] for i in TURN2_L.splitlines())
TURN4_L = """
. ... .
 .... .
..... .
..... .
..... .
..... .
..... .
""".strip()
TURN4_R = "\n".join(i[::-1] for i in TURN4_L.splitlines())
DOWN_LEFT = """
... . .
.... ..
 .... .
. ... .
 .... .
. ... .
. ... .
""".strip()
DOWN_RIGHT = "\n".join(i[::-1] for i in DOWN_LEFT.splitlines())
DOWN_MERGE = """
.......
.......
 ..... 
. ... .
 ..... 
. ... .
. ... .
""".strip()
DOWN = (". . . .\n" * 7).strip()
SPLIT = """
... ...
.. . ..
. ... .
. ... .
. ... .
. ... .
. ... .
""".strip()
TWO_SPLIT = """
. ... .
 . . . 
.. . ..
. ... .
. ... .
. ... .
. ... .
""".strip()
SIDE = """
.......
.......
.......
       
.......
.......
.......
""".strip()
SIDE_NOT = """
.......
.......
...0...
       
.......
.......
.......
""".strip()
DOWN_XOR_TOP = """
. ... .
. ... .
. ... .
 .... .
. ... .
.. . ..
. . . .
""".strip()
DOWN_CROSSING_TOP = """
. ... .
. ... .
..... .
 .... .
. ... .
.. . ..
. . . .
""".strip()
DOWN_XOR_BOTTOM = """
.. . ..
. .. ..
.. .. .
. . .. 
. .. ..
. ... .
. ... .
""".strip()
RIGHT_START_EMPTY = """
.......
.......
.......
...    
.......
.......
.......
""".strip()
RIGHT_START_FULL = """
.......
.......
.......
...0   
.......
.......
.......
""".strip()
END = """
... ...
... ...
... ...
... ...
.......
.......
.......
""".strip()
LEFT_BEND = """
.......
.......
.......
   ....
... ...
... ...
... ...
""".strip()


large_grid = """
 S S S S S S S S  -2
 P P P P P P P P  -1
6J D D D D D D D   0  - 0N
 BIG D D D D D D   1
6J BIJ D D D D D   2
 BIG BIJ D D D D   3
6J BIJ BIG D D D   4
 BIG BIJ BIJ D D   5
6J BIG BIG BIJ D   6
 BIJ BIJ BIJ BIJ   7
6J BIG BIJ BIJ BI7 8  - 1N
 BIG BIJ BIG BIG D 9  - N+1
6J BIG BIG BIJ B7D 10 - N+2
 BIG BIJ BIJ BIG1L 11
6J BIG BIJ BIJ B7A 12
 BIJ BIJ BIJ BIJ1L 13
6J BIJ BIG BIJ B7A 14
 BIG BIG BIJ BIJ1L 15
   BIJ BIJ BIJ B7A 16 - 2N
     BIJ BIG BIJ1L 17
       BIG BIJ B7A 18
         BIJ BIG1L 19
           BIJ B7A 20
             BIG1L 21
               B7A 22
                1L 23
                 A 24 - 3N
                 Z 25 - 3N+1
""".strip("\n").splitlines()


flag = "0011010101101000010100100011000100110011011010110110001001110101001100010110001001010011010111110100000101110010001100110101111101010100011010000011001101011111010000100011001101110011001101110101111101100010001100110110001100110100011101010101001100110011010111110111010001101000001100110111100101011111011000010011000100110001001100000101011101011111011011010011001101011111011101000011000001011111011000110011000001101110001101010111010001110010010101010110001101010100010111110100001101101001011100100110001101010101001100010111010001110011010111110011011000111000011000100110001001100110001100110011000100111001"
flag_matrix = [int(i) for i in flag]
tots = [1 for i in range(len(flag))]
large_grid = [[" "]*(2*len(flag) + 2) for i in range(3*len(flag)+4)]

for i in range(len(flag)):
    large_grid[0][2*i+1] = "S"
    large_grid[1][2*i+1] = "P"
    if i == 0:
        large_grid[len(flag)+2][-1] = "7"
        large_grid[len(flag)+3][-1] = "D"
        large_grid[len(flag)+4][-1] = "D"
    else:
        large_grid[2*i+len(flag)+3][-2] = "1"
        large_grid[2*i+len(flag)+3][-1] = "L"
        large_grid[2*i+len(flag)+4][-1] = "A"
    for j in range(i+1, len(flag)):
        large_grid[i+2][2*j+1] = "D"
    for j in range(len(flag)):
        large_grid[i+2*j+3][2*i+1] = "B"
        if os.urandom(1)[0]%2 == 1:
            tots[j] ^= flag_matrix[i]
            large_grid[i+2*j+2][2*i+1] = "J"
        else:
            large_grid[i+2*j+2][2*i+1] = "G"
        if i == len(flag) - 1 and j > 0:
            large_grid[i+2*j+3][2*i+2] = "7"
        else:
            if os.urandom(1)[0]%2 == 1:
                tots[j] ^= 1
                large_grid[i+2*j+3][2*i+2] = "8"
            else:
                large_grid[i+2*j+3][2*i+2] = "I"
for i in range(len(flag)):
    large_grid[2*i+2][0] = "60"[tots[i]]
large_grid[-1][-1] = "Z"
open('test.txt', 'w').write("\n".join("".join(j for j in i) for i in large_grid))

l, w = len(large_grid)*7, len(large_grid[0])*7

grid = [["."]*w for i in range(l)]
thing = {"S": START, "1": TURN, "2": TURN2_L, "3": TURN2_R, "4": TURN4_L, "5": TURN4_R,
         "A": AND, "O": OR, "X": XOR, "N": NOT, "L": DOWN_LEFT, "R": DOWN_RIGHT, "D": DOWN,
         "P": SPLIT, "C": CROSS, "M": DOWN_MERGE, "Q": TWO_SPLIT, "I": SIDE, "J": DOWN_XOR_TOP,
         "B": DOWN_XOR_BOTTOM, "G": DOWN_CROSSING_TOP, "6": RIGHT_START_EMPTY, "0": RIGHT_START_FULL,
         "Z": END, "7": LEFT_BEND, "8": SIDE_NOT}
def pt(tile, x, y):
    x *= 7
    y *= 7
    tile = tile.splitlines()
    for i in tile:
        for j,k in zip(i, range(y, y+7)):
            grid[x][k] = j
        x += 1
def export(grid):
    out = f"{w}/{l}/"
    out += "".join("".join(plants[j] for j in i) for i in grid)
    return out

for r,i in enumerate(large_grid):
    for c,t in enumerate(i):
        if t == " ":
            continue
        pt(thing[t], r, c)
open('out.txt', 'w').write(export(grid))


for r,i in enumerate(large_grid):
    for c,t in enumerate(i):
        if t == "S":
            pt([START_EMPTY, START_0][flag_matrix[c//2]], r, c)
open('player.txt', 'w').write(export(grid))