def num_to_ascii(n):
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return chr(a)

def unhex(n):
    return int(n, 16)

def eval_tower(tower):
    powers = 0
    while tower:
        b = tower.pop()
        if isinstance(b, str):
            x, y = map(unhex, tower.pop())
            a = unhex(b)
            if a % 2 == 1:
                powers += ord(num_to_ascii(a))
        else:
            x, y = map(unhex, b)
        if a % 2 == 0:
            powers = 0
        else:
            powers += ord(num_to_ascii(x+y)) - 1
        a = x + y
    return chr(powers)

def eval_towers(towers):
    cat = ""
    for tower in towers:
        cat += eval_tower(tower)
    return cat
with open('out.txt') as f:
    p = int(f.readline())
    print(eval_towers(eval(f.readline())))