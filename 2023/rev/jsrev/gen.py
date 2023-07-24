import json

font = json.loads(open('monogram-bitmap.json', 'rb').read())
font = {k: v for k, v in font.items() if ord(k) < 128}

font_bmp = {}
for f in font:
    bmp = [[0 for _ in range(8)] for _ in range(12)]
    for row, bits in enumerate(font[f]):
        for col in range(8):
            if bits & (1 << col):
                bmp[row][col] = 1

    font_bmp[f] = bmp

flag = "amateursCTF{asK_4nD_thr33_5h4ll_r3c31v3}"
print(len(flag))
baseX = 2
BASEY = 50
baseZ = 10
SPHERE_RADIUS = 0.2 

# each char is 12 by 8
# diameter of sphere is 0.4 -> dimensions scaled to 4.8 by 3.2

charX = baseX
charZ = baseZ
pts = []
# for c in flag[:8]:
#     bmp = font_bmp[c]
#     for x in range(12):
#         x_offset = x * SPHERE_RADIUS * 2
#         for z in range(8):
#             z_offset = z * SPHERE_RADIUS * 2
#             if bmp[x][z]:
#                 pts.append([charX + x_offset + SPHERE_RADIUS, BASEY, charZ + z_offset + SPHERE_RADIUS])
    
#     charZ -= 3

for c in flag:
    bmp = font_bmp[c]
    for x in range(12):
        x_offset = x * SPHERE_RADIUS * 2
        for z in range(8):
            z_offset = z * SPHERE_RADIUS * 2
            if bmp[x][z]:
                pts.append([charX + x_offset + SPHERE_RADIUS, BASEY, charZ + z_offset + SPHERE_RADIUS])
    BASEY -= 0.4

pts = [[round(x, 2) for x in pt] for pt in pts]
print(pts, len(pts))

with open("coords.json", "w") as f:
    f.write(json.dumps(pts))