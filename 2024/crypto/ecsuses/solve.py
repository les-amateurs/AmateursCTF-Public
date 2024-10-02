flagtxt = open('flagtxt').read()
names = ["y ui", "jpbm wkl", "gy q", "rh ytu", "mpsyx z"]
original = flagtxt
while flagtxt:
    # print(names, flagtxt[:3])
    l = 3
    while flagtxt.count(flagtxt[:l]) == flagtxt.count(flagtxt[:3]) and (original.count(flagtxt[l:l+4]) < 2 or l < 9):
        if flagtxt[:l] in names:
            flagtxt = flagtxt[l:]
            l = 3
            break
        l+=1
    if l > 4:
        names.append(flagtxt[:l-1])
        flagtxt = flagtxt[l-1:]
    elif l == 4 and flagtxt[:4] in names:
        flagtxt = flagtxt[4:]
    elif flagtxt[:3] == "rh ":
        flagtxt = flagtxt[6:]
        # print(flagtxt)
    elif l == 4:
        print(names, flagtxt[:3])
        break
print(len(names))
print(names)
# manually fix names from this point on, rest shouldn't be too hard