# jsrev

## Author: flocto

**Solves:** 18

**Points:** 490

---

Someone wanted this, so I delivered.
Have fun!

[jsrev.amt.rs](http://jsrev.amt.rs)

---

## Solution
If you turn around quickly enough, you'll see that the balls fall in an almost purposeful formation.

Checking the coordinates, you might not see much, but if you focus on each Y level, letters start to form. We know each ball has radius 0.2, so diameter of 0.4, and we can assume that 0.4 is the same size as each "pixel" in the characters.
```python
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

first_layer = Image.new("L", (8, 8), 255)
firstY = max(letters.keys())
baseX = min([x for x, z in letters[firstY]])
baseZ = min([z for x, z in letters[firstY]])
print(baseX, baseZ)
STEP_SIZE = 0.4

for x, z in letters[firstY]:
    x_step = round((x - baseX) / STEP_SIZE)
    z_step = round((z - baseZ) / STEP_SIZE)
    print(x, z, x_step, z_step)
    first_layer.putpixel((z_step, x_step), 0)

first_layer.save("first_layer.png")

second_layer = Image.new("L", (8, 8), 255)
secondY = firstY - 0.4
baseX = min([x for x, z in letters[secondY]])
baseZ = min([z for x, z in letters[secondY]])   
print(baseX, baseZ)

for x, z in letters[secondY]:
    x_step = round((x - baseX) / STEP_SIZE)
    z_step = round((z - baseZ) / STEP_SIZE)
    print(x, z, x_step, z_step)
    second_layer.putpixel((z_step, x_step), 0)

second_layer.save("second_layer.png")
```
First layer:

![first_layer](src/first_layer.png)

Second layer:

![second_layer](src/second_layer.png)

They make up `am`, the first two characters of the flag. We can then repeat this process for the rest of the layers, and we get the flag.

Through the power of increasing the size manually, we reach and $8n$ by 10 image, where $n$ is the number of layers. We can then read the flag using our eyes.

```python
flag_img = Image.new("L", (8 * len(letters), 10), 255) # n chars, 8 wide, 10 tall
STEP_SIZE = 0.4
baseX = 2 # min of all x's
baseZ = 10 # min of all z's

for c, y in enumerate(letters.keys()):
    for x, z in letters[y]:
        x_step = int((x - baseX) / STEP_SIZE)
        z_step = int((z - baseZ) / STEP_SIZE)
        flag_img.putpixel((z_step + c * 8, x_step), 0)

flag_img.save("flag.png")
```
Final flag:

![flag](flag.png)

```
amateursCTF{asK_4nD_thr33_5h4ll_r3c31v3}
```


### Note
This challenge was made in a few hours just to troll Chip who kept asking for Javascript rev.

Sorry for any people who raged at this as a result :joy:.