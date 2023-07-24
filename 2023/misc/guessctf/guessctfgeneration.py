from Crypto.Util.number import *
from Crypto.Util.strxor import strxor
from Crypto.Cipher import AES
import pyminizip
import zipfile
import random as rnd
import hashlib
import os


flocto = "\n\n\n\n\nFlocto hint count: "
count = 0
password = """this password is reallhhy creative
ecksdee this is password
yep 111 password is this
p!@#$%^&&*words!
so i need this to be 45 characters long so ye
23 characters lets gooo
decimal too op wow number bases!
eycks dee wow not me reusing pws
one two three four five six
26 alphabet password cool.
...ab ood ood ood ood ood krahs ybab ood ood ood ood ood krahs ybab
ok at this point i'm confident you're cheating... what the fuck
heh smol e moment
engineering
lol bet u didnt expect this one coming
sand384 :D oops this password sHould be secure!!
i had no idea what to do for this level so i just stole a challenge lmao
weLp. I TRIED OK? 4 TIMES!! :Pray:
complex
              

m33t_m3_1n_th3_m1ddl3!!ineversaiditwascenteredthough!
l1tt3rb0x. literally a litter box. i don't know what you expected.
greAt intentions.!'
y0u-foUnd_me!!!~~me;a5 wel1?
the last 5 levels are pretty fun. glhf.
columns-are *comma * the-best.
THE repeat of THE best LEVEL in EXISTENCE.
m 3 t a _ l 3 v 3 1 s _ r _ t h 3 _ b 3 s 7 .
abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ
idt anyone will make it here but dm HELLOPERSON#7543 if you did."""
files = ['tutorial_level.txt', 'level1.html', 'level2.mp4', 'level3.7z', 'level4.png', 'level5.zip', 'level6.py', 'level7.pdf', 'level8.tar', 'level9.FLAG', 'level10.tar.gz', 'level11.enc', 'level12', 'level13.log', 'level14.0w0', 'level15.mp3',
         'level16.c', 'level17.f01', 'level18.tiff', 'level19.space', 'level20.ico', 'level21.iso', 'level22.svg', 'level23.js', 'level24.css', 'level25.docx', 'level26.xml', 'level27.md', 'level28.mov', 'level29.FINALE.notreally', 'level30.potato', 'flag.txt']
dir = "no/"
zipdir = "yes/"
passwordlist = password.split("\n")

assert passwordlist[19] == "              "
zwnj = chr(8204)
zwj = chr(8205)


# LEVEL 0
f = open(dir + "tutorial_level.txt", "w")
writething = ""
pt2 = "01111110011011010110010100111011011000010011010100100000011101110110010101101100001100010011111100001010000010100111001101100101011000110110111101101110011001000010000001101000011000010110110001100110"
for i in pt2:
    writething += chr(8204 + int(i))
writething = writething + """here's some text:
take the md5 hash of this line and repeat it a few times.
here's some hex:
b21e2deeed503640cded74cfe5511796b21e2deeed503640cded74cfe5511796b21e2deeed503640cded74cfe5511796b21e2deeed503640cded74cfe5511796b21e2deeed503640cded74cfe5511796b21e2deeed503640cded74cfe55170f9dd7a0d8482321860948201bdc52176e5c169429c8970422fed991caac53f72eec63e418b9b355a60a49e4eef85257fffc13e5d8f9e23412fbf8954a6967165f3d372418685291623bf8815bb8c2772f6
It's a one time pad with the md5 hash of that line.
Cool, got the password yet?"""
f.write(writething)
f.close()

# LEVEL 1
count += 1
f = open(dir + "level1.html", "w")
hexes = passwordlist[1].encode()
random = os.urandom(len(passwordlist[1]))
writething = random.hex() + strxor(hexes, random).hex() + \
    "\nfeeling the guess already?\n\n\n\n\nFlocto hint count: 1"
f.write(writething)
f.close()

# LEVEL 2
f = open(dir + "level2.mp4", "w")
hexes = passwordlist[2].encode()
random = bytes.fromhex(
    (randomplaceholder := os.urandom(len(passwordlist[1])).hex())[::-1])
assert len(random.hex()) == len(hexes.hex())
writething = strxor(hexes, random).hex() + randomplaceholder + \
    "\n\nnow do it in reverse" + flocto + str(count)
f.write(writething)
f.close()

# LEVEL 3
f = open(dir + "level3.7z", "w")
hexes = passwordlist[3].encode()
g = open("pi10k.txt", "r")
pi = g.read()
g.close()
# I could hard code this as 3863e3d79f4cf21741bc53eddb15a64a
thing = hashlib.md5(pi[500:3000].encode()).digest()
writething = "pi[500:3000]\n" + \
    strxor(thing, hexes).hex() + flocto + str(count)
f.write(writething)
f.close()

# LEVEL 4
count += 3
f = open(dir + "level4.png", "w")
hexes = passwordlist[4].encode()
# SCREW THIS I AM GOING TO HARD CODE THIS >:(
# cite: dcode.fr fibonacci encoding
writething = "I would never fib-\nUnforgotten bits referencebtw\n2523414135 x8\ne62f657d012acf674c817e4d3962657c3e0ae2ef0876bc74673923662bc356ef62d1756d7b3ee232db6782fd4d" + \
    flocto + str(count) + "\n\nHint courtesy of flocto: dcode.fr"
f.write(writething)
f.close()

# LEVEL 5
count += 4  # flocto got a walkthrough smh
f = open(dir + "level5.zip", "w")
hexes = passwordlist[5].encode()
g = open(dir + "output.bmp", "w")
# 19 1000 43 56
# range(19, 1000, 43) ^ 56
outputwrite = ""
for i in range(1000):
    if i % 43 == 19:
        x = hex(hexes[i//43] ^ 56)[2:]
    else:
        x = hex(rnd.randint(0, 255))[2:]
    outputwrite += "0" * (2-len(x)) + x
g.write(outputwrite)
g.close()
writething = """Now you're getting the hang of it. Hold on tight.
19 1000 43 56
^ Number format improved courtesy of flocto
What do those numbers mean? No one knows. Good luck! Have fun! You're not getting past here. I don't even know how you got past the last one.""" + flocto + str(count)
f.write(writething)
f.close()

# LEVEL 6
f = open(dir + "level6.py", "w")
hexes = passwordlist[6].encode()
while True:
    try:
        a = os.urandom(len(hexes))
        writething = str(bytes_to_long(a)) + \
            strxor(a, hexes).hex() + flocto + str(count)
        assert strxor(a, hexes).hex()[0] in "abcdef"
        break
    except:
        pass
f.write(writething)
f.close()

# LEVEL 7
f = open(dir + "level7.pdf", "w")
hexes = passwordlist[7].encode()
while True:
    try:
        a = os.urandom(len(hexes))
        writething = str(oct(bytes_to_long(a))[
                         2:]) + strxor(a, hexes).hex() + flocto + str(count)
        assert strxor(a, hexes).hex()[0] in "abcdef"
        break
    except:
        pass
f.write(writething)
f.close()

# LEVEL 8
count += 1
f = open(dir + "level8.tar", "w")
hexes = passwordlist[8].encode()
a = bytes.fromhex(
    "0" + str(rnd.randint(10**(len(hexes)*2), 10**(len(hexes)*2 + 1))))
hexes = b"\x00" + hexes
writething = a.hex()[1:] + strxor(a, hexes).hex()[1:] + flocto + str(count)
f.write(writething)
f.close()

# LEVEL 9
# im sorry this one is also hardcoded.
# alphabet is otp key
count += 1
f = open(dir + "level9.FLAG", "w")
hexes = passwordlist[9].encode()
writething = """485b5817001b0210150a115416061d17161c10074811161a055e

cqlahwxemsnygknuohfdbnrlscqwscllgtzpivnjbzbwvlksnfcqzccqwgjbtwelmsnygknulbvngctwelcnqzrlknulbyqlslknulbzslknulvmlxzhblcqlslzslgcslzttiynsvkslahlgxwlbzgvcqwbflbblbhdfzginkcqldtzwgclucxwdqlsclucknubntrlsbcqzchblbhmbcwchcwngbnilzqwfbhslinhslyngvlswgjyqzccqwbdtzwgclucxwdqlsclucdzwswbknszgvwfbnssicnclttinhcqzcwxzgcbzizgicqwgjwfohbcqlslcnqltdinhvlxnvlfibltkbncqzcwxzgvnbnflcqwgjwcqwgeinhrlgncwxlvlrlsicqwgjbnkzsqzbmllgznglcwfldzvzgvcqzcwbzmnhccnxqzgjlbnmldsldzslvknsmtwgvjhlbbwgj""" + flocto + str(count)
f.write(writething)
f.close()

# LEVEL 10
f = open(dir + "level10.tar.gz", "w")
hexes = passwordlist[10].encode()
a = os.urandom(len(hexes))
out = strxor(hexes, a).hex()
base6 = ""
c = bytes_to_long(a)
while c > 0:
    base6 = str(c % 6) + base6
    c = c // 6
writething = out + base6 + flocto + \
    str(count) + "\n" * 10000 + "01111001001100000111010100101101011001100110111101010101011011100110010001011111011011010110010100100001001000010010000101111110\n\nYou found me... hopefully not too early. First half."
f.write(writething)
f.close()

# LEVEL 11
# smells of death
count += 4
f = open(dir + "level11.enc", "w")
hexes = passwordlist[11].encode()
a = len(hexes)
keys = []
revkeys = []
newpw = [hexes, b"", b"", b"", b""]
writething = ""
for i in range(4):
    keys.append(os.urandom(a))
    for j in range(a):
        newpw[i+1] = newpw[i+1] + long_to_bytes(newpw[i][j] ^ keys[i][j])
newpws = [newpw[4], b"", b"", b"", b""]
for i in range(4):
    revkeys.append(os.urandom(a)[::-1])
    for j in range(a):
        newpws[i+1] = newpws[i+1] + \
            long_to_bytes(newpws[i][j] ^ revkeys[i][a-j-1])
for i in keys:
    writething = writething + i.hex() + "\n"
for i in revkeys:
    writething = writething + i.hex() + "\n"
writething = writething + newpws[4].hex() + "\n" + "I decided it would be too mean to concatenate all of these into 1 line, also you should thank me that they're ordered." + \
    flocto + str(count) + "\nHint courtesy of flocto: flip half."
f.write(writething)
f.close()

# LEVEL 12
f = open(dir + "level12", "w")
# ill hard code this one as well since i lost gen code
# its just rsa but e=1
writething = "3552415884440737889887112998831225500018051198730770204051751110422155811904698329\nrsa :D glhf" + \
    flocto + str(count)
f.write(writething)
f.close()

# LEVEL 13
count += 1
f = open(dir + "level13.log", "w")
# word puzzle
writething = """[redacted] was planning to put [redacted] here but forgot. Go do [redacted]. 

The thing I was [redacted] to put here was aes but key=0. Too easy though, so instead [redacted]. Also the next level is pretty much [redacted] so good [redacted].

Oops I forgot that telling you the [redacted] makes the guessing [redacted]. I redacted it instead. For the record there are only 14 [redacted] so you're almost there! just gotta find one last [redacted]. If you get stuck, I'm sure social [redacted] the admins can solve it.

Anyways, I need to go [redacted] my [redacted]. Go [redacted] that password.""" + flocto + str(count) + "\nChall improvement provided by flocto"
f.write(writething)
f.close()


flocto = "\n\n\n\n\nFlocto hint count: \nOh there's a slight problem. Since these levels (14-29) were added after I did the flocto testrun, the hint count is not accurate. Therefore, I will give flocto's hint count for level 30 (final level) and we are done with this count. Good luck on the rest. And good luck on this one.\nCount: "
# LEVEL 14
level = 14
count += 15
f = open(dir + files[level], "w")
hexes = passwordlist[level].encode()
key = b""
key = b"\x00" * (16 - len(key)) + key
hexes = b"\x00" * (16 - len(hexes) % 16) + hexes
iv = b"\x00" * 16
aescbc = AES.new(key, AES.MODE_CBC, iv=iv)
encrypted_flag = aescbc.encrypt(hexes).hex()
writething = encrypted_flag + flocto + str(count)
f.write(writething)
f.close()
level += 1

flocto = ""
# LEVEL 15
f = open(dir + files[level], "w")
hexes = passwordlist[level].encode()
x = os.urandom(48)
xorthing = hashlib.sha384(x).digest()
enc = strxor(hexes, xorthing)
writething = x.hex() + enc.hex() + "\n\n" + "沙" * 384
f.write(writething)
f.close()
level += 1

# LEVEL 16
f = open(dir + files[level], "w")
hexes = passwordlist[level].encode()
enc = ""
for i in range(len(hexes)//2):
    enc += hex(hexes[2*i])[2:]
    x = hex(hexes[2*i] ^ hexes[2*i+1])[2:]
    enc += "0" * (2-len(x)) + x
writething = enc
f.write(writething)
f.close()
level += 1

# LEVEL 17
f = open(dir + files[level], "w")
hexes = passwordlist[level].encode()
ctxt = bytes_to_long(hexes)**3
x = len(hexes)
x *= 12
p, q = 0, 0
while p * q <= ctxt:
    p, q = getPrime(x), getPrime(x)
writething = "rsa's revenge:\n" + str(ctxt) + str(p*q)
f.write(writething)
f.close()
level += 1

# LEVEL 18
f = open(dir + files[level], "w")
writething = "i\n\nWow you guys hide your flags? Mine is in plane sight!\n\nassert len(password.split()) == 1"
f.write(writething)
f.close()
level += 1

# LEVEL 19
f = open(dir + files[level], "w")
writething = "              "
f.write(writething)
f.close()
level += 1

# LEVEL 20
f = open(dir + files[level], "w")
writething = os.urandom(5000).hex()
f.write(writething)
f.close()
level += 1

# LEVEL 21
f = open(dir + files[level], "w")
hexes = passwordlist[level].encode()
# print(hexes.hex())
writething = os.urandom(1231).hex()[1:] + hexes.hex() + os.urandom(9999).hex()[1:]
f.write(writething)
f.close()
level += 1

# LEVEL 22
f = open(dir + files[level], "w")
hexes = passwordlist[level].encode()
hexes = bytes_to_long(hexes)
for i in range(30):
    hexes += 2**rnd.randint(0, len(bin(hexes)[2:]))
writething = hex(hexes)[2:] + "\n\n30 bits added."
f.write(writething)
f.close()
level += 1

# LEVEL 23
# chars after zwj
f = open(dir + files[level], "w")
g = open("hamlet.txt", "r")
hamlet = g.read()
g.close()
writething = "Source (why am i even giving you this): https://www.opensourceshakespeare.org/views/plays/play_view.php?WorkID=hamlet&Scope=entire&pleasewait=1&msg=pl\n" + hamlet
f.write(writething)
f.close()
level += 1

# LEVEL 24
f = open(dir + files[level], "w")
writething = "You left something behind. Where is it?\n\nNot a riddle lol go back and find what you missed if you haven't *seen* it yet. Heh."
f.write(writething)
f.close()
level += 1

# LEVEL 25
f = open(dir + files[level], "w")
hexes = passwordlist[level].encode().hex()[::-1]
writething = hexes + \
    "\n\nThis one is really simple. I can't believe I didn't put this earlier."
f.write(writething)
f.close()
level += 1

# LEVEL 26
f = open(dir + files[level], "w")
writething = ""
hexes = passwordlist[level].encode().hex()
for i in hexes:
    writething = writething + i
    writething = writething + os.urandom(16).hex()[1:] + "\n"
writething = writething + "\n\nI'm clearly running out of ideas. That's why there are only 30 levels, after all. This one is not too complicated, you should be able to figure it out. Random random random random noise. Hmmm this has been a theme recently. I should switch that up a bit."
f.write(writething)
f.close()
level += 1

# LEVEL 27
f = open(dir + files[level], "w")
writething = ""
hexes = passwordlist[level].encode()
a = len(hexes)
keys = []
revkeys = []
newpw = [hexes]
newpw.extend([b""] * 1000)
for i in range(1000):
    keys.append(os.urandom(a))
    for j in range(a):
        newpw[i+1] = newpw[i+1] + long_to_bytes(newpw[i][j] ^ keys[i][j])
newpws = [newpw[-1]]
newpws.extend([b""] * 1000)
for i in range(1000):
    revkeys.append(os.urandom(a)[::-1])
    for j in range(a):
        newpws[i+1] = newpws[i+1] + \
            long_to_bytes(newpws[i][j] ^ revkeys[i][a-j-1])
for i in keys:
    writething = writething + i.hex() + "\n"
for i in revkeys:
    writething = writething + i.hex() + "\n"
writething = writething + newpws[-1].hex() + "\n\nYou know what to do. :)"
f.write(writething)
f.close()
level += 1

# LEVEL 28
f = open(dir + files[level], "w")
pw = "m 3 t a _ l 3 v 3 1 s _ r _ t h 3 _ b 3 s 7 ."
# print(files[1][9] + files[3][5] + files[1][8] + files[19][10] + files[0][8] + files[26][10] + files[23][6] + files[22][9] + files[15][10] + files[15][5] + files[24][9] + files[0][8] + files[0][4] + files[0][8] + files[0][0] + files[1][7] + files[13][6] + files[0][8] + "output.bmp"[7] + files[15][10] + files[24][10] + files[27][6] + files[25][7])
writething = "19 35 18 1910 08 2610 236 229 1510 155 249 08 04 08 00 17 136 08 5-17 1510 2410 276 257\n\nYour daily hint: 08 -> _\n\nUpdate: I have recieved word that I would be fired if I didn't put at least 32 levels because power of 2. I'll just assume this includes tutorial, so I'll import the level as your next level. Happy guessing!"
f.write(writething)
f.close()
level += 1

# LEVEL 29
f = open(dir + files[level], "w")
hexes = passwordlist[level].encode()
writething = "So... I need an extra level. Oh here's a dumb idea. What if you *hypothetically* hid the password to this in... oh I don't know, like some random data from the previous levels or something?\n\nNah that would be too mean. Okok what if HYPOTHETICALLY I hid the password in plain sight. Oh i already did that. OK OK FOR REAL THIS TIME WHAT IF... the password was a permutation of ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()abcdefghijklmnopqrstuvwxyz, in the order 4231. or something like that. Nah that would be crazy. Ok, what about this. What if I hid the password on youtube. *Plugs youtube channel link*. Please like and subscribe!!!!!!!!!!!!!! Ok but no for real what if I hid the password to this on the wayback machine. What if you took the ctf link and then like, went back in time. using a time machine. Or something. No but fr the really dumb idea would be to actually do level 11/27 this time, but like. Different. Y'know, swapping the order, byte swapping instead of hex swapping, all that stuff. Hmmmm ok but really what if the password was hidden in plain sight the whole time, in this very file. You just haven't figured it out yet. Knowing the answer really makes everything a lot easier, doesn't it. There's really no reason to go back to previous levels at this point. The only information you need is here. This will be consistent for the rest of the levels, although some of them might've been training you for the finale. I'm not sure what, but something is coming. Don't miss it."
f.write(writething)
f.close()
level += 1

# LEVEL 30
f = open(dir + files[level], "w")
hexes = ""
writething = "Good job on making it here. Two more *puzzles* to solve. Wait... puzzles?\nSee originally I was going to do password indexing. But then I thought... \"Nah, that's too similar to level 28\". Which is unfortunate. idt anyone will make it here but dm HELLOPERSON#7543 if you did. DM me all the passwords from level1.zip pw to level30.zip pw. I'll give you a hint as to where the password is located. See, since you made it too far, I thought it would've been too easy for you. Anything I put here you would viciously tear down, so long as the level were computationally feasible. Looking at you, level22 which is definitely not computationally feasible. Yeah so there's just a 3 hour timewall here dm me and expect a response 3 hours later. If I forget, just remember, this level is solvable without me. The next level is hintless, and will never get hints. Good luck. Have fun. Be prepared for the worst. Don't forget to finally extract that hidden information in the levels with extra hex. Use this key: abcdef. With this key you will be able to unlock the secrets of the universe and beyond. Just don't forget to use it."
f.write(writething)
f.close()


# LEVEL FINAL (Probably 30) oops now its 31 *boss music plays*
f = open(dir+"flag.txt", "w")
password = "THE QUICK BROWN FOX ATE THE LAZY DOG... wait that's not how it goes? Good job on geting this far by the way, I'm still not sure how. but yeah the flag is a bit further down, after jumping a bit, hmm did you decode the wrong thing? Good job go try again. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac convallis est, ac eleifend dui. Ut et tellus ac metus rhoncus aliquam id quis velit. Donec finibus sollicitudin ex, ac molestie sem semper quis. Aliquam accumsan libero ut finibus accumsan. Suspendisse in dui volutpat magna imperdiet egestas id ut justo. Suspendisse nulla mauris, bibendum sed condimentum sit amet, pulvinar posuere enim. Proin eu varius eros. Praesent posuere justo a velit pharetra luctus. Integer luctus libero eget ligula euismod, vitae euismod lectus ultrices. Donec tempus nunc nec mauris iaculis dictum. Aliquam sit amet neque sapien. Phasellus a bibendum risus. In lorem mi, congue quis lobortis in, varius eu ante. Mauris vel est sit amet nibh luctus bibendum id non diam. Nulla id diam quis leo pellentesque lobortis id quis ligula.".encode()
flag = "amateursCTF{i_legitimately_have_no_clue_how_you_guessed_your_way_here,but_good_job_ig_..._..._..._morse_code_next_time_maybe?}".encode()
password = bin(bytes_to_long(password))[2:]
flag = bin(bytes_to_long(flag))[2:]
flag = "0" + flag
password = "0" + password
writething = "Good job. You're almost there. Just one... small thing to decode. It's below. I'm waiting.\n\n"
for i in password:
    if i == "0":
        writething = writething + chr(8204)  # zwnj
    else:
        writething = writething + "aaaa"
    if rnd.randint(1, 10) == 3:
        writething = writething + "zzzz"
    if rnd.randint(1, 200) == 4:
        writething = writething + "\n"
    if rnd.randint(1, 2) == 2:
        writething = writething + "uwuuwuuwuuwu"
    if rnd.randint(1, 500) == 200:
        for j in flag:
            if rnd.randint(1, 3) == 1:
                writething = writething + "zzzz"
            if j == "0":
                writething = writething + "t"
            else:
                writething = writething + chr(8205)  # zwj
writething = writething + "aa" + \
    "zzazzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\nzzzzzzzzz"
f.write(writething)


pyminizip.compress(dir + "flag.txt", None, zipdir +
                   "level31.zip", passwordlist[-1], 9)

for i in range(len(passwordlist) - 1, 0, -1):
    if i != 5:
        pyminizip.compress_multiple([dir + files[i], zipdir + "level" + str(
            i+1) + ".zip"], [], zipdir + "level" + str(i) + ".zip", passwordlist[i-1], 9)
    elif i == 5:
        pyminizip.compress_multiple([dir + files[i], zipdir + "level" + str(i+1) + ".zip",
                                    dir + "output.bmp"], [], zipdir + "level" + str(i) + ".zip", passwordlist[i-1], 9)


filenames = [dir + files[0], zipdir + "level1.zip"]


with zipfile.ZipFile(zipdir + "guessctf.zip", mode="w") as archive:
    for filename in filenames:
        archive.write(filename, arcname=filename.split("/")[-1])

# pyminizip.compress_multiple([dir + files[0], zipdir + "level1.zip"], [], zipdir + "guessctf.zip", None, 9)
