from random import randint

ns = [randint(0, 255) for _ in range(1337)]

print(f"var input = [_]u8{{ { str(ns)[1:-1] } }};")

ns = sorted(ns)
print(bytes(ns).hex())