import base64
import itertools
print(base64.b64decode("TEFSUlk==").decode())

print('77777') # lol

b = b'56789'
b = bytes([x ^ 0x60 for x in b])
print(b.decode())

alpha = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
for key in itertools.product(alpha, repeat=5):
    key = bytes(key)
    
    x, y = 0, 0
    for k in key:
        while k:
            m = k & 0b11
            if m & 1:
                x += 1
            else:
                x -= 1
            if m & 2:
                y += 1
            else:
                y -= 1

            k >>= 2
    
    if x == 5 and y == 3:
        print(key)
        break

# CLOCK has levenshtein distance of 3 from UNL0CK
# LARRY-77777-YWUVX-NO732-CLOCK