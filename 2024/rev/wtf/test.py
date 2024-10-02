a = int.from_bytes(b'sbg', 'big')
b = int.from_bytes(b'love', 'big')
c = int.from_bytes(b'lcg', 'big')
seed = 0xf10c70 

print((a * seed * seed + b * seed + c).bit_length())