with open('out.txt', 'r') as f:
    data = bytes.fromhex(f.read())
    primes = [32, 79, 243] # factor len(data)
    product = 32*79*243 # factor len(data)
    for i in primes:
        if 10 <= i <= 100:
            keylen = i
            blocksize = product//keylen
            xorchart = []
            for j in range(blocksize):
                xorchart.append("")
            for j in range(blocksize):
                xorchart[(j*keylen) % blocksize] = data[j*keylen] ^ data[0]
            for j in range(256):
                guess = ""
                for k in xorchart:
                    guess += chr(j ^ k)
                if "amateursCTF" in guess:
                    z = guess.index("amateursCTF")
                    print(guess[z:z+70])
                    exit(0)
