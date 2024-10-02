from Crypto.Util.strxor import strxor
from pwn import process
import string

r = process(['python3', 'pilfer-techies.py'], level='error')


def get_blocks(msg):
    r.sendlineafter(b'> ', b'1')

    r.sendlineafter(b': ', msg.hex().encode())

    ct = r.recvline().strip().decode()
    ct = bytes.fromhex(ct)

    blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]
    return blocks


def get_flag():
    r.sendlineafter(b'> ', b'2')
    ct = r.recvline().strip().decode()
    ct = bytes.fromhex(ct)

    blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]
    return blocks

# initial message to calculate which j causes the loop to occur after 1 iteration
msg1 = b''
for i in range(256):
    blk = bytearray(16)
    blk[0] = i
    idx = i % 16
    for j in range(16):
        if idx != 15:
            blk[idx + 1] = j
        msg1 += bytes(blk)
        for k in range(1, 16):
            if k == idx + 1:
                continue
            blk[k] = 1
        msg1 += bytes(blk)
        for k in range(1, 16):
            if k == idx + 1:
                continue
            blk[k] = 0
# print(len(msg1)) # 131072

enc_flag = get_flag()
dec = [b'' for _ in enc_flag]
r.close()

while not all(dec):
    r = process(['python3', 'main.py'], level='error')
    enc_flag = get_flag()
    blocks = get_blocks(msg1)
    valid_chars = string.printable.encode() + b"\x00"
    # wanted = set([int(line.split()[1]) for line in flag_lines])

    # find the valid j for each i that causes the loop to occur after 1 iteration
    valid = {}
    for i in range(256):
        block = blocks[32*i:32*(i+1)]
        for j in range(16):
            if strxor(block[2*j], block[2*j+1]).startswith(b'\x01' * 14):
                # print(i, j, block[2*j], block[2*j+1],
                #       strxor(block[2*j], block[2*j+1]))
                valid[i] = j

    # send all valid j with 0x10 offsets to server for otp
    msg2 = b''
    for i in range(256):
        blk = bytearray(16)
        blk[0] = i
        idx = i % 16

        for j in range(16):
            if idx != 15:
                blk[idx + 1] = valid[i] + j * 0x10
            msg2 += bytes(blk)

    # print(len(msg2)) # 65536
    blocks = get_blocks(msg2)

    # print(wanted)

    # try decrypting with all blocks in the encrypted flag
    for enc_idx, enc_block in enumerate(enc_flag):
        dec_block = b''
        for i in range(256):
            block = blocks[16*i:16*(i+1)]
            for j in range(16):
                if block[j][-1] == enc_block[-1]:
                    tst = strxor(block[j], enc_block)
                    if all(c in valid_chars for c in tst[:15]):
                        # we got lucky, first byte is 0x*f
                        dec_block = bytes([i]) + tst[:15]
                        break
                    elif all(c in valid_chars for c in tst[:14]):
                        # reconstruct full block from i and j
                        dec_block = tst[:14]
                        idx = i % 16
                        
                        dec_block = dec_block[:idx] + bytes([valid[i] + j * 0x10])  + dec_block[idx:] # the byte that causes the loop after 1 iteration
                        dec_block = bytes([i]) + dec_block # original first byte
                        break
        
        if dec_block:
            print(enc_idx, enc_block, dec_block)
            dec[enc_idx] = dec_block
    r.close()
    print(dec)
                
