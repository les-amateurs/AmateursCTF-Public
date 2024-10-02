mod = 1000000007

def solve_r(a):
    valid = []
    for i in range(256):
        x = 97 * i
        for j in range(256):
            if pow(x, j, mod) == a:
                valid.append((i, j))
    
    return valid

output = eval(open('output.txt').read())

valid = solve_r(output[0])

for r1, r2 in valid:
    d = pow(r2, -1, mod - 1)
    
    flag = [
        (pow(c, d, mod) * pow(r1, -1, mod) - output[i - 1]) % mod
        for i, c in enumerate(output)
    ]
    flag[0] = 97
    print(bytes(flag).decode())