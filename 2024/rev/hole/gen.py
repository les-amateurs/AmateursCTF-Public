import random

# https://arxiv.org/pdf/2212.03494.pdf
# https://esolangs.org/wiki/%F0%9F%95%B3%EF%B8%8F

msg = open('msg.txt').read().strip()

inds = []

for i in range(random.randint(800, 900)):
    a = random.randint(0, len(msg) - 1)
    b = random.randint(0, len(msg) - 1)
    inds.append((min(a, b), max(a, b)))

for i, j in inds:
    msg = msg[:i] + msg[i:j+1][::-1] + msg[j+1:]

open('enc.txt', 'w').write(msg)

code = "❗" * len(msg.splitlines())

for i, j in inds:
    code = f"⚠️*{code}*{i}*{j}*"

code = f"❓*{code}*"

open('code.🕳️', 'w').write(code)