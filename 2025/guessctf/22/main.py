#!/usr/local/bin/python

import random
print("quiz time!")


a = input("At the time of writing this, how many levels are left to be written? ")
b = input("Which crypto challenge did the flag come from? ")
c = input("This isn't a real question but I think the answer is. ")
d = input("Final question: what did the spreadsheet message say? ")




answers = ("4", "flcg", " four", "I THINK YOU SHOULD CHECK THE OTHER SHEET.") # yeah fuck this im not changing the 'flcg' answer lmao it's technically correct from sctf


if (a, b, c, d) == answers and random.randint(1,10) == 10:
    print("youresosmart!heresapassword:heart:")
else:
    print("something doesn't seem right... are you sure you've completed all the previous levels?")