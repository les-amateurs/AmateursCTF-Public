#!/usr/local/bin/python3

from typing import Any
def decor(func):
 def wrapper(*args, **kwargs):
  if hasattr(args[0], 'n'):
   n = args[0].n
  elif hasattr(args[0].__class__, 'n'):
   n = args[0].__class__.n
  else:
   raise TypeError("Error: bit count not found")
  out = func(*args, **kwargs)
  if type(out) == int:
   return out % (2 ** n)
  if hasattr(out, '__iter__'):  # for divmod
   return type(out)(x % (2 ** n) for x in out)
 return wrapper

to_decor = ['__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__add__', '__sub__', '__mul__', '__mod__', '__pow__', '__lshift__', '__rshift__', '__and__', '__xor__', '__or__', '__floordiv__', '__truediv__', '__divmod__']
to_decor.extend(['__r' + x[2:] for x in to_decor])
to_decor.extend(['__i' + x[2:] for x in to_decor])
uint_to_copy = vars(int).items()
uint_to_copy = {k: v for k, v in uint_to_copy if k not in to_decor}
uint_to_copy.update({k: decor(v) for k, v in vars(int).items() if k in to_decor})
# no such thing as float division for uints
uint_to_copy['__truediv__'] = uint_to_copy['__floordiv__']

def uint_repr(self):
 if hasattr(self.__class__, 'n'):
  n = self.__class__.n
 else:
  raise TypeError("Error: bit count not found")
 return f'uint{n}({int(self) % (2 ** n)})'

uint_to_copy['__repr__'] = uint_repr

def mk_class(n):
 return type('uint%d' % n, (int,), {'n': n, **uint_to_copy})

for x in range(8, 257, 8):
 locals()['uint%d' % x] = mk_class(x)

def letters(input_thingo):
 return any(i.lower() in "abcdefghijklmnopqrstuvwxyz()@" for i in input_thingo)

def shit_input(prompt):
 abc = input(prompt)
 if letters(abc):
  exit("HI YOU ARE NOT SUPPOSED TO HAVE LETTERS!!! KTHX")
 return abc

while True:
 a = "uint" + str(int(shit_input("First uint? ")))
 a1 = int(shit_input("First value? "))
 exec(f"a2 = {a}({a1})")
 b = "uint" + str(int(shit_input("Second uint? ")))
 b1 = int(shit_input("Second value? "))
 exec(f"b2 = {b}({b1})")
 c = shit_input("Operation? ")
 assert len(c) <= 10, "Hi that's not really an operation is it"
 print(f"Evaluating: {a2} {c} {b2}")
 res1, res2 = eval(f"a2 {c} b2"), eval(f"int(a2) {c} int(b2)")
 if res1 != res2:
  print(f"The results were different! {res1 = }, {res2 = }")
  continue
 else:
  print(f"The result was: {res1}")
 break