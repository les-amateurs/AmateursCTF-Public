import zipfile

zfile = zipfile.ZipFile('flag.zip', 'r')

print(zfile.comment)

print(zfile.read("flag/"))

namelist = zfile.namelist()
for name in namelist:
    info = zfile.getinfo(name)
    if info.comment:
        print(name, zfile.read(name), info.comment)

for i in range(1024):
    name = "flag/flag" + str(i) + ".txt"
    if namelist.count(name) != 1:
        print(name)
        # this part can't be done with zipfile afaik, but extract this file name WITHOUT overwriting and the last part of the flag is in there
        # Part 4: _Zips}
        
# amateursCTF{z1PP3d_in5id3_4_laY3r_0f_Zips}