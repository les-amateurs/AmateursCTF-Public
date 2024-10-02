import random
random.seed(143414121337)
tr = {}
a = "abcdefghijklmnopqrstuvwxyz      "
for i in range(128):
    tr[i] = "".join(random.choices(a, k=random.randint(4, random.randint(5, 8))))
    while tr[i].count(" ") != 1 or tr[i][0] == " " or tr[i][-1] == " ":
        tr[i] = "".join(random.choices(a, k=random.randint(4, random.randint(5, 8))))
with open('tr', 'w') as f:
    f.write(str(tr))
del tr
tr = eval(open('tr').read())
flagtxt = open('flagtxt.py').read()
# exec(flagtxt)
with open('flagtxt', 'w') as f:
    f.write(flagtxt.translate(tr))