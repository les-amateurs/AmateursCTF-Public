import crccheck
crc32 = crccheck.crc.Crc32.calc
data = open('bad-3-corrupt_flag.tar.xz', 'rb').read()

# tr "\t \-_" " \t_\-"

dd = b''
for c in data:
    if c == 0x20:
        dd += b'\t'
    elif c == 0x09:
        dd += b' '
    elif c == 0x5f:
        dd += b'-'
    elif c == 0x2d:
        dd += b'_'
    else:
        dd += bytes([c])

s1 = 6, 8
t1 = 8

c1 = crc32(dd[s1[0]:s1[1]])
dd = dd[:t1] + c1.to_bytes(4, 'little') + dd[t1+4:]

s2 = -8, -2
t2 = -12
c2 = crc32(dd[s2[0]:s2[1]])
dd = dd[:t2] + c2.to_bytes(4, 'little') + dd[t2+4:]

open('solve.tar.xz', 'wb').write(dd)

import subprocess
proc = subprocess.run(['xzcat', '-d', 'solve.tar.xz'], stdout=subprocess.PIPE, check=False)
out = proc.stdout

# find png
start = out.find(b'\x89PNG')
end = out.find(b'IEND')

open('solve.png', 'wb').write(out[start:end+4])