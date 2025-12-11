from Crypto.Util.number import *
from Crypto.Util.strxor import strxor
from Crypto.Cipher import AES
from zf import mkzip, fake_mkzip
import string
import zipfile
import random as rnd
import hashlib
import os

password = """
.;,;.{ts pmo}
needed a budget excuse me i guess so here is your guess capture the flag level replacement
1462429366668283501
theoritization_ofl0c4l_3nTangleMentation
9b0he0iu)(CUjhjkbf1oeufhiOJOISFDSFUOIu9riCCqv()#3#
.;,;.{M\/|\A}
hiddeN_sh3etS_leak
sotuprasyvnimerataelenaod
l3l_x0R_k3y_w1th_steg0_1s_a_l1ttl3_t0O_many_lay3rs_0f_ObfuScatIOn.
D6@hK#1wR5!z
w3ll_n0t_L!t3rA11y_Th15-t8m4. but like. flOcTo's nuclear corrupted this pw. it's all floctos fault!!
something smth entropy ig
amateursCTF{aN_1t3r!7avE_fi/7iTe_f1n3-FlN3_c1ph3r}
the music security team solved this level in 15 minutes
amateursCTF{n0_th3_fl4g_1s_n0T_th3_Same_1f_y0U_w3r3_w0ndeRing_533e72a10}amateursCTF{po0r_m4ns_lambd4_c4lculus_45b538a09}.;,;.{it_seems_you_started_this_ctf_'sane'._Lets_see_if_you_can_end_it_as_sane_as_you_started.}
me_personally_i_would_never_hehe
egikqrstvwxy
50rry 1 d0n'7 5p34k 1337
very brutable.
iguessyouwinthisrandomstring???????whatseventhepointoftheselotteriesanyways?
floctollm amateursCTF sh3etS
Can you tell me a bit more about the context?
youresosmart!heresapassword:heart:
guess basis ensue issue truss sushi
""".strip().splitlines()
files = """
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
flag.txt
""".strip().splitlines()

extra_files = [0, 1, 2, 3, ["qr.png"], ["mvm.csv"], 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
dir = "no/"
zipdir = "yes/"

def writelevel(writething):
    global level
    with open(dir + files[level], 'w') as f:
        f.write(writething)
    level += 1

level = 0
# LEVEL 0
writething = "ah, the obligatory tutorial level. what is the flag from last guessctf? i hope you have a working memory. i sure don't, i keep getting confused between this guessctf and last guessctf... i hope that doesn't impact any of the levels."
writelevel(writething)

# LEVEL 1
writething = "millions of excuses, one for me, one for you, maybe one for us this time?\n\n"

def dictionary_shift(t, k):
    t = t.split()
    d = open('dictionary.txt').read().lower().splitlines()
    new_t = []
    for i in t:
        idx = d.index(i)
        idx += k
        idx %= len(d)
        new_t.append(d[idx])
    return " ".join(new_t)
    
text = "of course the password to this level is something stupid like why would it not be anyways comma space here is the password colon " + password[level]
writething += dictionary_shift(text, 2026) # one extra shift just for you <3
writelevel(writething)

# LEVEL 2
writething = "ok since i leaked some guessctf 2024 passwords i'm making you do them again now. well i tried to but no one did smileyctf guessctf so um yeah. or at least the ones which aren't trivially reversable from the challenge source files that got publicized loooooooooooooooooool."
writelevel(writething)

# LEVEL 3
writething = "(looking over this level again i think it's just straight up impossible but it's funny so i'm keeping it)\n\ni asked floctollm for a level and he just told me this: \"I was a nuclear physicist before i took 17 pounds of brunt force to my toe which hurt a lot owwwee oweuuhhhc\""
writelevel(writething)

# LEVEL 4
writething = "my qr code needed a quilt."
writelevel(writething)

# LEVEL 5
writething = "found this file... it's just people saying \"mvm\"...???"
writelevel(writething)

# LEVEL 6
writething = "someone leaked the password to this level on the ctf.gg website... im pretty sure they said something about guessctf leaks?"
writelevel(writething)

# LEVEL 7
writething = """across:
1. with a prepended e i am area, from that, with a prepended t i am intentional, from that, with a prepended a i am the greatest puzzle game of all time (or something like that)
2. shade of primary color inverse to a color that is not autistic
3. slang for a bright red ingot
4. fitting description for a thursday movie
5. more alliterative version of ____ of the sweats
down:
1. dish with elbows, in the morning, rain, or under the weather
2. spinnysy
3. plural of e^i - cos
4. dark sister
5. internet alternative to contractual scamming
read this grid as monarchies in asia would"""
writelevel(writething)

# LEVEL 8
writething = "i asked chatgpt for a custom stego format... i mean i guess it's custom? i guess you either see it x you don't. 'you already know the key' ahh challenge"
writelevel(writething)

# LEVEL 9
writething = """""The Key Beneath the Layers""

They said, ""It's simple--just some math,""
But every block obscures the path.
A quiet war of byte and bit,
Where guesses fail, and patterns split.

The plaintext once was pure and clean,
Now veiled in rounds, no trace is seen.
A subtle box, a shifting scheme,
What once was real now feels a dream.

You try to trace the hidden thread,
Through tangled steps the cipher spread.
Each round, a mask—no hint, no clue,
Each XOR smirks, ""I know more than you.""

Columns mix, the rows all shift,
A labyrinth with no clear lift.
The key? It morphs and multiplies,
Its purpose wrapped in thin disguise.

You search for flaws--timing, mode,
A leaking edge, a cracked decode.
A byte reused, a nonce betrayed,
One fatal slip, encryption flayed.

Each test you run, each script you write,
Draws shadows closer to the light.
And when you finally glimpse the truth,
It isn't luck--it's skill, it's proof.

Now rest not yet--decode, delight,
But start with these to crack the night:

Here's something useful for your quest:
e0d173c12ab26a11bcc8b5f77ece07fb  
f3757e6d50f586c8e6a28ac58524a875""".replace('""', '"')
writelevel(writething)

# LEVEL 10
writething = "reduce reuse recycle"
hexes = password[level].encode()
hexes = bytes_to_long(hexes)
for i in range(30):
    hexes += 2**rnd.randint(0, len(bin(hexes)[2:]))
writething += "\n\n" + hex(hexes)[2:]
writelevel(writething)

# LEVEL 11
hexes = password[level].encode()
writething = bin(int(os.urandom(1231).hex(),16))[5:] + bin(int(hexes.hex(),16))[2:] + bin(int(os.urandom(9999).hex(),16))[7:]
while len(writething) % 8:
    writething = bin(int(os.urandom(1231).hex(),16))[5:] + bin(int(hexes.hex(),16))[2:] + bin(int(os.urandom(9999).hex(),16))[7:]
writelevel(hex(int(writething,2))[2:])

# LEVEL 12
writething = f"""[A finite Cipher]:
I decided to create an oracle for some new cipher(s) I invented! Try and figure out how it works. Wait you want source? That's not how this works! Go figure it out on your own. It should be fin{'e'*43273}."""
writelevel(writething)

# LEVEL 13
writething = "i lost the flag in the amazon rainforest 3 years ago. the new update goes hard though."
writelevel(writething)

# LEVEL 14
writething = "you get to take a break from guessctf to play real ctf. concatenate flags from the following challenges:\n\n"
writething += """1x crypto challenge
1x rev challenge
1x misc challenge

oh you thought the recipe would be more specific lol. hf."""
writelevel(writething)

# LEVEL 15
writething = "me when pollution"
writelevel(writething)

# LEVEL 16
writething = "00001010101000001111011110"
writelevel(writething)

# LEVEL 17
writething = "sorry i don't speak leet"
writelevel(writething)

# LEVEL 18
writething = "i think the pw is very brutable."
writelevel(writething)

# LEVEL 19
writething = """four score and twelve hours ago-"""
writelevel(writething)

# LEVEL 20
writething = "3 words."
writelevel(writething)

# LEVEL 21
writething = "but if guessctf isn't the password then what is? maybe it's 'music security department'?\n\ni asked chatgpt and it seems to know!"
writelevel(writething)

# LEVEL 22
writething = "45666"
writelevel(writething)

# LEVEL 23
writething = "yellow green black black green black black green black green black black green green black yellow black green green black yellow yellow black black green green green green black black"
writelevel(writething)

# LEVEL FLAG
flag = ".;,;.{ts pmo}"
flagtuah = b"amateursCTF{ksdjhaskljfhasklfjh}"
writething = f"""so much work and effort was put into the smileyctf guessctf, and it all amounted to nothing. bad ctftime rating, no one made any progress, wasted time and setup. but i still found a use for it, helping out the environment by reducing reusing and recycling. this is almost the end. will there any winners this time? who knows. but you, the solver, have one last challenge to face. go and claim your prize.

{bytes(i^j for i,j in zip(hashlib.sha256(flag.encode()).digest(), flagtuah)).hex()}"""
writelevel(writething)
# print(password)


# zip file stuff here

mkzip([dir + files[-1]], zipdir + "level24.zip", password[-1])

for i in range(23, 0, -1):
    extra = []
    if isinstance(extra_files[i], list):
        extra = extra_files[i]
    mkzip(extra + [zipdir + f'level{i+1}.zip', dir + files[i]], zipdir + f"level{i}.zip", password[i-1])

filenames = [dir + files[0], zipdir + "level1.zip"]

with zipfile.ZipFile(zipdir + "guessctf.zip", mode="w") as archive:
    for filename in filenames:
        archive.write(filename, arcname=filename.split("/")[-1])
