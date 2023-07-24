import json
from PIL import Image

coords = json.load(open("static/coords.json", "r"))
# split by Y
letters = {}
for x, y, z in coords:
    if y not in letters:
        letters[y] = []
    letters[y].append((x, z))

print(letters.keys())

flag_img = Image.new("L", (8 * len(letters), 10), 255) # n chars, 8 wide, at least 10 tall
STEP_SIZE = 0.4
baseX = 2
baseZ = 10

for c, y in enumerate(letters.keys()):
    for x, z in letters[y]:
        x_step = int((x - baseX) / STEP_SIZE)
        z_step = int((z - baseZ) / STEP_SIZE)
        flag_img.putpixel((z_step + c * 8, x_step), 0)

flag_img.save("flag.png")
