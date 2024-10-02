from Crypto.Util.number import *
from Crypto.Util.strxor import strxor
from Crypto.Cipher import AES
from zf import mkzip
import string
import zipfile
import random as rnd
import hashlib
import os

password = """tutorial level
styli
ilovexorilovexor
picoCTF{4ny0n3_g0t_r1scv_h4rdw4r3?_LGUfwl8xyMUlpgvz}
uwu{i_love_blind_format_string_pwn}
fyS0i[^te)xa'writ
 four
dead fish
heart in triangle
sraurkodsusuvubknrshsdkus
kroot-why_are_you_reading_this?..!
tractordbftw
this isn't the real password (it's redacted)
DYNAMIC_PASSWORD
wow lcg is not cryptographically secure idor but better!??!?
yeah this is the first part.&qq&&q&&&*q*rHELPFEDIVERSEISIMPOSSIBLE
wow i am so creative reusing/rehashing guessctf from last year but with a twist omg.
C8@rT#0pA8!q

0h, 7h1s, n0w this: th1s i5 th3 r3al chall3nge
11226123801071024-42955919249611025
idt anyone will make it here but dm HELLOPERSON#7543 if you did.
DYNAMIC_PASSWORD
36294260117
mbcdgfaeljkoinspqrthuvwxyz
i can count!
xoloitzcuintles
parity_matters! !this is lsb stego on text. i was too lazy to make the text make sense.
wow is this a guessctf password"????? i guess you'll have to wait and see!
DYNAMIC_PASSWORD
41 28 10 07 50 31 51 61 31 18 21 19 27 41 71 81 60 13
r౦񫴡""".splitlines()
files = """0.hex
1.py 
2.xor
3.zip
4.tar
5.gz
6.xz
7.fish
8.enc
9.exe
10.docx
11.mp4
12.bat
13.xlsx
14.accdb
15.jar
16.wks
17.pub
18.mov
19.sql
20._
21.__
22.___
23.swift
24._____
25.c
26.class
27.bmp
28.img
29.heic
30.igloo
31.png
flag.txt""".splitlines()

extra_files = [0, 1, 2, ['rev'], 4, 5, 6, 7, 8, 9, 10, 11, ['server.py'], 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
dir = "no/"
zipdir = "yes/"

def writelevel(writething):
    global level
    if 1 <= level <= 24:
        writething += "\n" * int(password[25].encode().hex()[level-1], 16)
    with open(dir + files[level], 'w') as f:
        f.write(writething)
    level += 1

level = 0
# LEVEL 0
writething = f"hi. password is `tutorial level`. here's python code. \n{open('zf.py').read()}"
writelevel(writething)

# LEVEL 1
writething = "what is the plural of floctopus? floctopi of course. what else? oh, hi you're here. go find the password already bruh."
writelevel(writething)

# LEVEL 2
text = b"abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba"*49
new_text = b""
for i in range(len(text)):
    if i % 2 == 0:
        new_text += chr(text[i]^ord(password[level][(i//2) % len(password[level])])).encode()
    else:
        new_text += chr(text[i]).encode()
writething = "hi. you're at level 2. good job. so far so good. take the flag, it's below."
writething += "\n" + new_text.hex()
writelevel(writething)

# LEVEL 3
writething = "writing... thirty or so unique levels is quite hard. being original is quite hard. these are all supposed to be really dumb puzzles that i made that are way to vague... but we promised this year that there would be less... of certain types of puzzles and more variety. i'm afraid those will exist but they will be few and far between. SO I JUST STOLE A REV CHALLENGE LMAO!"
writelevel(writething)

# LEVEL 4
writething = "connect to chal.amt.rs:4141"
writelevel(writething)

# LEVEL 5
writething = "three is my favorite prime. \n33333333339333333333333333033333333333333303333333633333335333333333333333333333336333333353333333633333335333333333333333633333336333333323333333633333333333333333333333033333333333333333333333633333334333333333333333533333333333333393333333333333338333333333333333933333333333333333333333333333334333333333333333833333336333333313333333333333335333333363333333333333336333333333333333633333336333333363333333433333333333333323333333633333334333333363333333533333333333333303333333633333333333333333333333633333"
writelevel(writething)

# LEVEL 6
writething = "2 + 2 ="
writelevel(writething)

# LEVEL 7
writething = "2 x 2 = "
writelevel(writething)

# LEVEL 8
writething = "2 ^ 2 = "
writelevel(writething)

# LEVEL 9
writething = """"sorry. do this stupid crossword that i constructed that is the most bullshit thing to ever have existed ever.
across:
1. unique quartets of a valentines outing?
2. multiplayer numbers puzzle excluding you specifically?
3. derivative by parts, in the order of 54213?
4. a blind spychologist?
5. questionable singleplayer numbers puzzles for a blind kid?
down:
1. many of these crosswords, starting with a little bit of friction?
2. my favorite wordle guess of the wrong parity?
3. apeiodirc anteater?
4. perfectly normal?
5. demands, with an aneurysm?"""
writelevel(writething)

# LEVEL 10
writething = "KROOT. woah. who's that. i've never heard of them before. maybe they have the password? maybe i know they have the password? maybe they don't know they have the password? maybe everything was always a lie?"
writelevel(writething)

# LEVEL 11
writething = "did you know that one of the factors of 901970847337419660290927657186220952416910975009987102830336151801272768113159236255527093281259263146438935793415170361905675406941589040843998320801720819501275714715741575595630206785103156282992431486926359151201888527687132461560140649339642704354959907998847037233154976553453452612310707926313611768754626253186177237546556838111595025348052278234004519836805866841883686273820180521782799634024191693799724695697423747365773293138074612051201787528031617710311653510098318970858735226472742726245012293308905304338160995748491340094845819048602053629955444778488565248737181452736819121181129131414288467769119710979798613320880363242511575815652092705102581908486663806596331253066695533821567520438474085699872298452470619038307219115548278019977265422366607032030016370751538691740246264220009219166615691816063905086406554223652870944829718389741159668949513188562734809436857679132973528055212972849535983686360235679784863085987694330773278513242584467467701654101680900029742295254013308053044837025653256876127160917419537422570896035285252051660633972630777589687617872705312085519981721365942174413780333598928059389749108095979571749458514801064603684026610315280297406757721129461928261105716602860092380689232187 is 28137900489948020308871352493074278532829580225855646849868029193362517037593466569672024701684418204252417381296510882859072045939120480799095764770705448813032655722088664397295670945516090995494456108148011819736870572004818737645151395990025744255206048874566563136984853831704196911981326514092696318656693747576406325611214217591614151030885456451394268613151276757405012708202399358981687212244146326214857656439070554378699738277091567261352709584649518069824915868847355060591007631411355695712224100624054069284946365299986384620686451439561383032901500572576802805621734182213245388375147339304185722163621? i hear it's exactly 30087 from the password."
writelevel(writething)

# LEVEL 12
writething = "ok... port: 1413"
writelevel(writething)

# LEVEL 13
writething = "half of half of half. who wins? the best, obviously. occam's razor always wins.\n"
pw = "9vu9gubuuriouvcjh1eifhofhvjhdjksf"
for i in pw.encode():
    writething += str(i)
pw = "98098buvyoiwufoiu09uf90ugoi2uerkljflkjglkhflksjf"
for i in pw.encode().hex():
    writething += str(i) + rnd.choice("0123456789abcdef") + rnd.choice("0123456789abcdef") + rnd.choice("0123456789abcdef") + rnd.choice("0123456789abcdef") + rnd.choice("0123456789abcdef") + rnd.choice("0123456789abcdef") + rnd.choice("0123456789abcdef")
pw = "".join(i for i in writething[::8])
password[level] = pw
writelevel(writething)

# LEVEL 14
writething = "port: 1431"
writelevel(writething)

# LEVEL 15
writething = "i've been reminded that these levels are sorely missing out on the one thing i liked most about last year's guessctf: flavortext. yeah, it's wayyy too hard without flavortext. although, my recommendation says that you could probably solve this level without... the flavortext. not even the clue, for that matter. do with that what you will.\nf0c3CPQTgDfWCEGaqD5Do"
writelevel(writething)

# LEVEL 16
writething = "and here i am. left abandoned. less than 24 hours before the ctf start, nothing. everyone busy with other stuff, no one willing to write FUN ORIGINAL VARIETY for guessctf. ok. well. this is probably getting old by now. it was probably old last year. hex is below."
writething += "\n"
key = b"\x00" * 16
hexes = b"\x00" * (16 - len(password[level]) % 16) + password[level].encode()
iv = b"\x00" * 16
ofb = AES.new(key, AES.MODE_OFB, iv=iv)
writething += ofb.encrypt(hexes).hex()
writelevel(writething)

# LEVEL 17
writething = "me: give me a password.\n"
writething += "chatgpt: here you go! 0be47f67-e8d2-4eb0-8ec3-328ba0a5556f"
writelevel(writething)

# LEVEL 18
writething = "that wasn't even a password. come on chatgpt, give me a real password! oh, you want a real password? oh, you want a real password?? OH, YOU WANT A REAL PASSWORD???\n"
writething += "i'll give you a password.\n"
writething += "now brute force this one :P"
writelevel(writething)

# LEVEL 19
writething = "now you probably think it's been easy so far. the first 10? maybe a little difficult. 11-18? probably really easy for you! so, ready for a challenge? i hope you are. channel your inner LLM. unscramble the below:\n"
writething += " h 3hr0hlsn37lcliwi  g1: hns ta 3ahst1 05het"
writelevel(writething)

# LEVEL 20
writething = "well, it's level 20. i think this one should be easier. Oh, sorry, impossible. the password to this level is the concatenated answers to the indiv round of ccamb 2024 (im gonna be honest i don't know why the problems/solutions aren't released yet, but this is very convenient for this purpose. also please dont harass anyone in order to obtain these please kthx.). good luck!"
writelevel(writething)

# LEVEL 21
writething = "bro why am i writing these levels at the last minute im literally out of ideas. im so uninspired rn."
writelevel(writething)

# LEVEL 22
writething = "cuneiformly at random... :scream: 128 bit ice cream is the worst.\n"
rnd.seed(os.urandom(10))
newthing = "\n".join(hex(rnd.getrandbits(2048))[2:].zfill(512) for i in range(20))
thing = {i:j for i,j in zip(b'0123456789abcdef', " 𒐕𒐖𒐗𒐘𒐙𒐚𒐛𒐜𒐝𒐬𒐭𒐯𒐰𒐱𒑈")}
writething += newthing.translate(thing)
password[level] = str(rnd.getrandbits(128))
writelevel(writething)
rnd.seed(os.urandom(10))

# LEVEL 23
writething = "i love enumerating primes. i also love numbers greater than 10^10. i love both things separately. i know what the password to level 23 is."
writelevel(writething)

# LEVEL 24
alpha = list('abcdefghijklmnopqrstuvwxyz')
new_alpha = []
while len(new_alpha) < 26:
    new = rnd.choice(alpha)
    while new in new_alpha:
        new = rnd.choice(alpha)
    new_alpha.append(new)
t = {ord(i):j for i,j in zip(alpha, new_alpha)}
a = list(b'ilosthegam')
b = list('losthegami')
tl = {i:j for i,j in zip(a,b)}
writething = "rot(1434) Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus vel iaculis quam, a placerat nisi. Vivamus placerat eros orci, id finibus metus viverra commodo. Ut luctus sollicitudin orci, eleifend auctor tortor finibus sit amet. Morbi condimentum nisi nulla, at tristique purus consequat maximus. Nulla vel ex at arcu fringilla cursus. Nam dignissim dolor sit amet auctor faucibus. Mauris posuere non quam vitae viverra. Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur odio diam, sagittis sit amet pretium eu, ullamcorper at augue. Donec hendrerit volutpat tellus, nec facilisis magna dictum sed. Curabitur elit est, consectetur vitae feugiat eget, condimentum vitae erat. Aenean in cursus elit. Duis placerat laoreet convallis. Suspendisse vel mi eget nunc malesuada mattis in ut nulla. Praesent at tortor ligula. Etiam convallis nisi dolor, at lacinia mauris varius in. Nam ut iaculis nisl. Donec imperdiet eros neque, ac laoreet quam vulputate ac. Cras feugiat varius turpis, nec accumsan diam mattis sit amet. Nunc at justo iaculis velit condimentum consectetur. Praesent sed sollicitudin velit, a sagittis ex. Fusce elementum elementum lacinia. In aliquet diam eu imperdiet ullamcorper. Aenean et augue suscipit, blandit velit sed, elementum risus. Pellentesque sed orci blandit, auctor massa vitae, pharetra nisi. Sed non ultrices sapien. Cras iaculis, tellus eget consectetur interdum, ante leo vulputate ante, non laoreet erat velit mollis nulla. Vivamus tempus, lectus in dictum maximus, felis dolor semper felis, eget luctus lacus nisl ac ipsum. Praesent accumsan urna eget tellus vehicula, quis fringilla nulla convallis. Integer ante eros, vehicula ac orci vel, feugiat sodales neque. Vivamus venenatis mollis ex nec lobortis. Aenean consectetur felis vel tincidunt eleifend. Nam accumsan tincidunt mi posuere pharetra. Sed iaculis leo eu augue sollicitudin sodales et eget dolor. In hac habitasse platea dictumst. Quisque laoreet aliquam enim non suscipit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam eget quam sed libero facilisis feugiat nec sit amet nibh. Fusce at vulputate quam. Morbi varius id nisi ac lobortis. Duis at pellentesque justo, a congue lorem. Ut luctus augue vel lacus vehicula scelerisque. Fusce a sodales dolor. Aenean finibus justo eget quam auctor, eget congue odio hendrerit. Vestibulum sit amet condimentum urna, non scelerisque tellus. ! abcdefghijklmnopqrstuvwxyz. Nulla sit amet ante a velit iaculis congue. In pretium vel massa sed tempor. Sed et suscipit sapien. Vivamus sodales risus eu leo molestie viverra. Phasellus vestibulum lacus eget erat hendrerit lobortis. Quisque metus leo, molestie ut aliquet id, egestas eu tellus. Praesent vitae interdum massa. Fusce mauris nisi, bibendum eget cursus quis, lacinia eget lacus.".lower().translate(tl).replace("!", "i lost the game. the password is")
writething = writething.translate(t)
writething = "at this point.. you know what to do... right??\n" + writething
writelevel(writething)

# LEVEL 25
writething = "im lagging a bit behind on these levels. gotta pick up the pace! there's still like, 7 more to go, including flag.txt. That's like, a whole 1 more level than last year!!"
writelevel(writething)

# LEVEL 26
writething = "hi. i feel like i'm talking to no one at this point... but i think there's not enough guessy cipher!!!! please go decrypt the below:\n"
writething += "um... ok no cipher today. the password is my favorite bomb party word or something."
writelevel(writething)

# LEVEL 27
writething = "that's quite... strange. quite eccentric, if i do say so myself, there's something peculiar going on below. It can't be flat, it's not uniform, there's no smooth pattern? what is this, is it like an elaborate bipartite prank?\n"
even = [i for i in string.printable if ord(i) % 2 == 0]
odd = [i for i in string.printable if ord(i) % 2 == 1]
writething += "".join(rnd.choice(even) if ord(i) % 2 == 0 else rnd.choice(odd) for i in bin(bytes_to_long(password[level].encode())).replace("b", ""))
writelevel(writething)

# LEVEL 28
writething = "be there or be square. i said the password to this level somewhere. were you there? oh ok you're a square."
writelevel(writething)

# LEVEL 29
password[level] = "".join(password[i] for i in range(level))
writething = "i thought this would be fun. i thought this would be easy. it turns out, coming up with all these ideas is neither. i've probably spent more time making this than you have solving it, and that's... honestly, i don't mind. at least you're here. if anyone even is.... like, what? who is even here. how did you get here? was the flavortext too helpful?? i wish someone could prove to me that they had all the passwords up to this point. maybe a simple meow would do it."
writelevel(writething)

# LEVEL 30
writething = "it's done. there are no more ideas. they're all dead. i know we promised more variety this year, but... i can't write web challenges. i can't write pwn challenges. i can't write rev challenges. and the other organizers have better things to do than write guessctf. i've returned to the one constant i've had in my life, the alphabet. the alphabet is my favorite pri-"
writelevel(writething)

# LEVEL 31
writething = "you know, i was going to provide a nice, easy path to the flag from here. except there's a problem. i lost the password to my flag. please help find it! i heard it was like, very short tho (<4 characters?!?), so can u pls pls pls recover it kthx."
writelevel(writething)

# LEVEL FLAG
flag = "amateursCTF{th3_r3turn_0f_gu3ssCtf...wait_wtf_why_are_you_here_help}".encode()
writething = "oh! you found my password! that's quite unexpected, even if it was only 3 characters long. i found this random string on the ground, i hope it means something to you cuz it sure doesn't mean anything to me!\n\n"
writething += hex(154650847133623320596362330585445312780631977420263671901443321044102169615649081719685254483990609500830142160207647855230844378952761426584027005989655432351740781665841305151834541854941378585504348633363358673978841008479441195444707772825915057400018321560021559624361307550623532737902133301181566097377842046875314871631872)[2:-2]
writelevel(writething)
# print(password)


# zip file stuff here

mkzip([dir + files[-1]], zipdir + "level32.zip", password[-1])

for i in range(31, 0, -1):
    extra = []
    if isinstance(extra_files[i], list):
        extra = extra_files[i]
    mkzip(extra + [zipdir + f'level{i+1}.zip', dir + files[i]], zipdir + f"level{i}.zip", password[i-1])

filenames = [dir + files[0], zipdir + "level1.zip"]

with zipfile.ZipFile(zipdir + "guessctf.zip", mode="w") as archive:
    for filename in filenames:
        archive.write(filename, arcname=filename.split("/")[-1])