code = open('code.🕳️').read().strip()
enc = open('enc.txt').read().strip()

code = code.split("*")

inds = []
for c in code:
    if c.isnumeric():
        inds.append(int(c))

inds = [(inds[i], inds[i+1]) for i in range(0, len(inds), 2)]

for i, j in inds[::-1]:
    enc = enc[:i] + enc[i:j+1][::-1] + enc[j+1:]

print(enc)