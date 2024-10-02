from Crypto.Util.number import *
from os import urandom
from string import ascii_lowercase as l
assert l == "abcdefghijklmnopqrstuvwxyz"
assert l.upper() == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
assert 1 < 2 < 6 < 7 < 9
assert 0 < 1 < 3 < 4 < 8
assert 3 < 4 < 7 < 8 < 9
assert 1 < 3 < 5 < 6 < 8
assert 0 < 2 < 3 < 6 < 7
assert (False <= False)
five = True + True + True + True + True
eight = five + True + True + True
e = five
n = 18731219289365451707395636596932254785677284594241109384800519389765106459345198545307011538411135923983879307000082960497061573724484567698585810539175072481288419304792074964613950793815384754832573175733310816392601565047732601148570012113050316423371167528572635358592163106667443934027544361784714556003266645830505556816115063227354574250199833021831126540372973814103449456562741465330689161914406832557989
flag = bytes_to_long((f"amateursCTF{{ba90253f8d2e25ef248c8a53bb339ae6b9a6646c66d3daecad5afd8e22c9643c10183f27c56efac917cdf83b2b62913d0e78689728e7aff5b1d71a9030f6d2002574f14d44991619{urandom(eight).hex()}}}").encode())
assert pow(flag, e, n) == 16998117284736388988402359681534302513962520091855118349594747852789348011551473959601954783974924035775178285977850381661589161002538289319033181766239368259877771519052266077607756515892404214393118418774836141905429782186529527212901243802008339338314073103827489640419299434509824599973703744029780440646652670296709656956091986772740104122949867454651661357823674661448011901779083315610359914549546741460284