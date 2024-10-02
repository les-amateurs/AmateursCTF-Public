import random

r = random.Random('five nights as freddy')
flag = "amateursCTF{p1ckL3-is_not_the_goat_l4rrY_is_m0R3_\:goat:ed}"

flag = list(flag.encode())

r.shuffle(flag)
print(flag)

# r_nums = zip(r.randbytes(len(flag)), flag) 
r_nums = r.randbytes(len(flag))
print(r_nums)
r_nums = list(map(int.__xor__, r_nums, flag))
print(r_nums, len(r_nums))