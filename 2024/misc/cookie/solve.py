from Crypto.Util.number import long_to_bytes
from galois import GF
import numpy as np

F = GF(2)
server_map = open('out.txt').read()
w, l, server_map = server_map.split("/")
w, l = int(w), int(l)
flen = 616

grid = [[] for i in range(l)]
for i in range(len(server_map)//2):
    grid[i//w].append(server_map[2*i:2*i+2])

def export(grid):
    out = f"{w}/{l}/"
    out += "".join("".join(plants[j] for j in i) for i in grid)
    return out

k = 1
coeff_matrix = [[0]*(flen-k) for i in range(flen-k)]
target_vector = [0]*(flen-k)

for i in range(flen):
    for j in range(flen):
        if grid[(i+2*j+2)*7+2][(2*i+1)*7+1] == ";3":
            if j >= k and i >= k:
                coeff_matrix[j-k][i-k] = 1
        if i == flen - 1 and j > 0:
            continue
        else:
            if j >= k and grid[(i+2*j+3)*7+2][(2*i+2)*7+3] == "$0":
                target_vector[j-k] ^= 1
for i in range(flen):
    if grid[(2*i+2)*7+3][3] == ";3" and i >= k:
        target_vector[i-k] ^= 1
print("amateursCTF{" + long_to_bytes(int("0" + "".join(str(i) for i in np.linalg.solve(F(coeff_matrix), F(target_vector))), 2)).decode() + "}")