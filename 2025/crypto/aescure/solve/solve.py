from Crypto.Cipher import AES


for i in range(128):
    for j in range(128):
        for k in range(128):
            key = bytes([97, 109, 97, 116, 101, 117, 114, 115, 67, 84, 70, 123, i, j, k, 125])
            cipher = AES.new(key, AES.MODE_ECB)
            pt = b'\x00' * 16
            if cipher.encrypt(pt).hex() == "5aed095b21675ec4ceb770994289f72b":
                print(key)

"""
5aed095b21675ec4ceb770994289f72b
"""