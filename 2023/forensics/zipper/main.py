import zipfile
import string
import random

zfile = zipfile.ZipFile('flag.zip', 'w')
zfile.comment = b'So many flags... So many choices...\nPart 1: amateursCTF{z1PP3d_'

zfile.mkdir('flag')

r = random.randint(0, 1023)
zfile.writestr('flag/flag' + str(r) + '.txt', "Part 4: _Zips}", compress_type=zipfile.ZIP_DEFLATED)
zfile.printdir()

# for i in range(128):
#     rn = random.randint(0, 1023)
#     while rn == r:
#         rn = random.randint(0, 1023)
    
#     zfile.writestr('flag/flag' + str(rn) + '.txt', ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(10, 50))), compress_type=zipfile.ZIP_DEFLATED)

zfile.writestr('flag/', "Part 2: in5id3_4_", compress_type=zipfile.ZIP_DEFLATED)
zfile.getinfo('flag/').comment = b'Part 3: laY3r_0f'

for i in range(1024):
    zfile.writestr('flag/flag' + str(i) + '.txt', ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(10, 50))), compress_type=zipfile.ZIP_DEFLATED)

for i in range(10):
    zfile.writestr('flag/../flag', "red herring XD", compress_type=zipfile.ZIP_DEFLATED)
