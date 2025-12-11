from Crypto.Cipher import AES as _AES
from Crypto.Util.number import long_to_bytes as _l2b
from Crypto.Util.number import bytes_to_long as _b2l
from hashlib import sha256 as _sha256
from hashlib import md5 as _md5
from os import mkdir as _mkdir
from os import path as _path

def mkzip(items, dest, pwd=None):
    zip = b""
    for i in items:
        zip += i.split("/")[-1].encode() + b"\x00"
        try:
            with open(i, 'rb') as f:
                contents = f.read()
                length = _l2b(len(contents))
                lenlen = _l2b(len(length))
                if len(lenlen) != 1:
                    raise ValueError("File {i} is too large.")
        
                zip += lenlen + length + contents
        except Exception as e:
            print(f"{e}\nError reading file: {i}. Check if the file exists? Also support for folders has not been added.")
            return
    
    if pwd:
        key = _sha256(pwd.encode()).digest()
        key_checksum = _md5(pwd.encode()).digest()
        nonce = b"\x00" * 16
        enc = _AES.new(key, _AES.MODE_GCM, nonce=nonce)
        zip = key_checksum + enc.encrypt(zip)

    with open(dest, 'wb') as f:
        f.write(zip)

def unzip(directory, dest, pwd=None):
    if dest[-1] != "/":
        dest += "/"
    with open(directory, 'rb') as f:
        zip = f.read()
        if pwd:
            key = _sha256(pwd.encode()).digest()
            key_checksum = zip[:16]
            if key_checksum != _md5(pwd.encode()).digest():
                raise ValueError("Incorrect Password")
            nonce = b"\x00" * 16
            dec = _AES.new(key, _AES.MODE_GCM, nonce=nonce)
            zip = dec.decrypt(zip[16:])
        if not _path.exists(dest):
            _mkdir(dest)
        while zip:
            filename, zip = zip.split(b"\x00", 1)
            lenlen = zip[0]
            length = _b2l(zip[1: 1 +lenlen])
            contents, zip = zip[1 + lenlen: 1 + lenlen + length], zip[1 + lenlen + length:]
            print(filename)
            with open(dest + filename.decode(), 'wb') as g:
                g.write(contents)
    
def main():
    mkzip(['guessctfgeneration.py'], 'guessctf', 'guessing is easy')
    unzip('guessctf', 'guessctf.unz', 'guessing is easy')
    
if __name__ == "__main__":
    main()
