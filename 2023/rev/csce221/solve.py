data = open("main.coredump", "rb").read()
# intended solve idea is find main from header and original main binary
# then find location inside the coredump
# from there, find pointer to list struct, and follow to individual nodes
# since operations were all run without interruption, all nodes are together XD
# malloc no randomize XD

# here's a oneshot

start = data.find(b"a" + b"\x00" * 7)
flag = b"\x00"

while flag[-1] != b"}"[0]:
    flag += bytes([data[start]])
    start += 0x20

print(flag.decode())
