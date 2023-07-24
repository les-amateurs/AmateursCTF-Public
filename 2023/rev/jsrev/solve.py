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

# first_layer = Image.new("L", (8, 8), 255)
# firstY = max(letters.keys())
# baseX = min([x for x, z in letters[firstY]])
# baseZ = min([z for x, z in letters[firstY]])
# print(baseX, baseZ)
# STEP_SIZE = 0.4

# for x, z in letters[firstY]:
#     x_step = round((x - baseX) / STEP_SIZE)
#     z_step = round((z - baseZ) / STEP_SIZE)
#     print(x, z, x_step, z_step)
#     first_layer.putpixel((z_step, x_step), 0)

# first_layer.save("first_layer.png")

# second_layer = Image.new("L", (8, 8), 255)
# secondY = firstY - 0.4
# baseX = min([x for x, z in letters[secondY]])
# baseZ = min([z for x, z in letters[secondY]])   
# print(baseX, baseZ)

# for x, z in letters[secondY]:
#     x_step = round((x - baseX) / STEP_SIZE)
#     z_step = round((z - baseZ) / STEP_SIZE)
#     print(x, z, x_step, z_step)
#     second_layer.putpixel((z_step, x_step), 0)

# second_layer.save("second_layer.png")

flag_img = Image.new("L", (8 * len(letters), 10), 255) # n chars, 8 wide, 10 tall
STEP_SIZE = 0.4
baseX = 2
baseZ = 10

for c, y in enumerate(letters.keys()):
    for x, z in letters[y]:
        x_step = int((x - baseX) / STEP_SIZE)
        z_step = int((z - baseZ) / STEP_SIZE)
        flag_img.putpixel((z_step + c * 8, x_step), 0)

flag_img.save("flag.png")
