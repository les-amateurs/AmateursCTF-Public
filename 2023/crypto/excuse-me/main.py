import random

def shuffle(thing):
    random.shuffle(thing)
    return thing

def getAlpha():
    shuffled = shuffle(list(range(97, 123)))
    new_alpha = {i:shuffled[i-97] for i in range(97, 123)}
    return new_alpha

all_ascii = {chr(i):getAlpha() for i in range(256)}

with open('popular.txt', 'r') as f:
    wordlist = f.read().splitlines()
    real_wordlist = []

with open('data.txt', 'r') as f:
    data = f.read()

while len(real_wordlist) < len(data):
    real_wordlist += wordlist

random.shuffle(real_wordlist)
writestring = ""
print("done processing first part")

for i in data:
    if ord(i) > 255 and i not in all_ascii:
        all_ascii[i] = getAlpha()
    text = " ".join(real_wordlist[:10])
    real_wordlist = real_wordlist[10:]
    text = text.translate(all_ascii[i])
    writestring += text + ". "
print("done processing data")

with open('bloat.txt', 'w') as f:
    f.write(writestring)