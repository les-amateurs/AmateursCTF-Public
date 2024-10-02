# valid = []
# for i in range(100000):
#     s = str(i).zfill(5)
#     if sum([int(c) for c in s]) == 35 and len(set(s)) == 5:
#         valid.append(s.encode())

# alpha = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for v in valid:
#     i = 0x60
#     v_x = bytes([v[j] ^ i for j in range(5)])
#     if all(vx in alpha for vx in v_x):
#         print(v, v_x, hex(i))

# alpha = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# import itertools

# tx, ty = 5, 3
# for key in itertools.product(alpha, repeat=5):
#     key = bytes(key)
    
#     x, y = 0, 0
#     for k in key:
#         while k:
#             m = k & 0b11
#             if m & 1:
#                 x += 1
#             else:
#                 x -= 1
#             if m & 2:
#                 y += 1
#             else:
#                 y -= 1

#             k >>= 2
    
#     if x == tx and y == ty:
#         print(key)

def levenshtein(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        dp[i][0] = i
    for j in range(len(b) + 1):
        dp[0][j] = j
    
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + (a[i - 1] != b[j - 1])
            )
        
    return dp[-1][-1]

print(levenshtein('UNL0CK', 'CLOCK'))
