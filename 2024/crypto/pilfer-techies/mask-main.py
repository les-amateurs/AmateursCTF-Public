import hmac
from os import urandom
from Crypto.Util.strxor import strxor
from Crypto.Util.number import *


class Cipher:
    def __init__(self, key: bytes):
        self.key = key
        self.block_size = 16
        self.rounds = 256

    def F(self, x: bytes):
        return hmac.new(self.key, x, 'md5').digest()[:15]

    def encrypt(self, plaintext: bytes):
        plaintext = plaintext.ljust(((len(plaintext)-1)//self.block_size)*16+16, b'\x00')
        mask = urandom(len(plaintext))
        ciphertext = b''

        for i in range(0, len(plaintext), self.block_size):
            block = plaintext[i:i+self.block_size]
            idx = 0
            for _ in range(self.rounds):
                L, R = block[:idx]+block[idx+1:], block[idx:idx+1]
                L, R = strxor(L, self.F(R)), R
                block = L + R
                idx = R[0] % self.block_size
            ciphertext += block
        ciphertext = bytes_to_long(ciphertext) ^ bytes_to_long(mask)

        return hex(ciphertext)[2:].zfill(len(plaintext)*2), mask.hex()


key = urandom(16)
cipher = Cipher(key)
flag = open('flag.txt', 'rb').read().strip()
masks = []

print("pilfer techies")
while True:
    choice = input("1. Encrypt a message\n2. Get encrypted flag\n3. Exit\n> ").strip()
    if choice == '1':
        pt = input("Enter your message in hex: ").strip()
        pt = bytes.fromhex(pt)
        ct, msk = cipher.encrypt(pt)
        print(ct)
        masks.append(msk)
    elif choice == '2':
        ct, msk = cipher.encrypt(flag)
        print(ct)
        masks.append(msk)
    else:
        print(*masks,sep='\n')
        break

print("Goodbye!")