from test import get_patch_info
from delta_patch import apply_patch_to_buffer

def remove_hash(delta, sz):
    _, _, _, _, _, _, hashalg, hashsize, _ = get_patch_info(delta)
    print(hashalg, hashsize)
    header = delta[:14] + sz 
    return header + delta[16 + 4 + hashsize:]

patch = b"\x50\x41\x33\x30\xc0\x08\x97\xfc\xfd\x3c\xda\x01\x18\x23\x68\x83\x00\x80\x52\x00larry-killed-this!!!\x01\xca\x00\xb7\x03\x88\x69\xb3\xfa\xf4\x89\x36\xa5\xdd\x8c\x01\xd1\xda\x4d\x88\x11\x69\x4c\xbb\x71\x7d\xda\x75\x6a\x37\x2a\xd2\x88\x11\x91\x22\x4e\x66\xde\xa0\x31\x3d\x22\xcc\x9b\xd6\xae\x47\xb4\x39\xb1\x56\x01"

buf = b'amateursCTF{'
try:
    out = apply_patch_to_buffer(buf, patch)
    print(out)
except Exception as e:
    print(e)

print(patch)
print(get_patch_info(patch))

patch = remove_hash(patch, b'h\x13\x02')
print(patch)
print(get_patch_info(patch))

out = apply_patch_to_buffer(buf, patch)
print(out)