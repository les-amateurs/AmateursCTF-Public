from pickle import *
import pickletools
import types


def encrypt(s):
    b = ''.join(format(ord(i), '08b') for i in s)
    b = (b + '1')[::-1]
    n = int(b, 2)
    return n.to_bytes(len(s) + 1, 'big')

def decrypt(b):
    n = int.from_bytes(b, 'big')
    b = bin(n)[::-1][:-3]
    s = ''
    for i in range(0, len(b), 8):
        s += chr(int(b[i:i+8], 2))
    return s

assert decrypt(encrypt('hello')) == 'hello'

keywords = [
    'builtins',
    'print',
    'map',
    'input',
    'len',
    'any',
    'str.encode',
    'list',
    'random',
    'seed',
    'shuffle',
    'randbytes',
    'int.__xor__',
    'int.__or__',
    'int.__ne__',
    'list.__getitem__',
]

enc = {
    k: encrypt(k) for k in keywords
}

def gen_stack_global(module, name):
    return GET + b'0\n' + \
                SHORT_BINBYTES + bytes([len(enc[module])]) + enc[module] + \
            TUPLE1 + REDUCE + \
            GET + b'0\n' + \
                SHORT_BINBYTES + bytes([len(enc[name])]) + enc[name] + \
            TUPLE1 + REDUCE + \
            STACK_GLOBAL

enc_flag = [138, 13, 157, 66, 68, 12, 223, 147, 198, 223, 92, 172, 59, 56, 27, 117, 173, 21, 190, 210, 44, 194, 23, 169, 57, 136, 5, 120, 106, 255, 192, 98, 64, 124, 59, 18, 124, 97, 62, 168, 181, 61, 164, 22, 187, 251, 110, 214, 250, 218, 213, 71, 206, 159, 212, 169, 208, 21, 236]

enc_flag_pickle = MARK 
for i in enc_flag:
    enc_flag_pickle += INT + (str(i) + '\n').encode()
enc_flag_pickle += LIST


payload = PROTO + b'\x04' + \
            GLOBAL + b'types\nFunctionType\n' + \
            MARK + \
                GLOBAL + b'types\nCodeType\n' + \
                MARK + \
                    INT + b'1\n' + \
                    INT + b'0\n' + \
                    INT + b'0\n' + \
                    INT + b'4\n' + \
                    INT + b'8\n' + \
                    INT + b'67\n' + \
                    SHORT_BINBYTES + b'\x62' + b't\x00\xa0\x01|\x00d\x01\xa1\x02}\x01t\x02|\x01\x83\x01d\x00d\x00d\x02\x85\x03\x19\x00d\x00d\x03\x85\x02\x19\x00}\x00d\x04}\x02t\x03d\x05t\x04|\x00\x83\x01d\x06\x83\x03D\x00]\x11}\x03|\x02t\x05t\x00|\x00|\x03|\x03d\x06\x17\x00\x85\x02\x19\x00d\x07\x83\x02\x83\x017\x00}\x02q\x1d|\x02S\x00' + \
                    MARK + \
                        NONE + \
                        UNICODE + b'big\n' + \
                        INT + b'-1\n' + \
                        INT + b'-3\n' + \
                        UNICODE + b'\n' + \
                        INT + b'0\n' + \
                        INT + b'8\n' + \
                        INT + b'2\n' + \
                    TUPLE + \
                    MARK + \
                        UNICODE + b'int\n' + \
                        UNICODE + b'from_bytes\n' + \
                        UNICODE + b'bin\n' + \
                        UNICODE + b'range\n' + \
                        UNICODE + b'len\n' + \
                        UNICODE + b'chr\n' + \
                    TUPLE + \
                    MARK + \
                        SHORT_BINUNICODE + b'\x04' + '🔥'.encode() + \
                        SHORT_BINUNICODE + b'\x04' + '🤫'.encode() + \
                        SHORT_BINUNICODE + b'\x04' + '🧏'.encode() + \
                        SHORT_BINUNICODE + b'\x04' + '🎵'.encode() + \
                    TUPLE + \
                    UNICODE + b'dill-with-it\n' + \
                    SHORT_BINUNICODE + b'\x04' + '📮'.encode() + \
                    INT + b'0\n' + \
                    SHORT_BINBYTES + b'\x0c' + b'\x00\x01\x0c\x01\x1a\x01\x04\x01\x14\x01 \x01' + \
                    EMPTY_TUPLE + \
                    EMPTY_TUPLE + \
                TUPLE + \
                NEWOBJ + \
                GLOBAL + b'builtins\nglobals\n' + \
                    EMPTY_TUPLE + \
                REDUCE + \
                SHORT_BINUNICODE + b'\x04' + '📮'.encode() + \
            TUPLE + \
            NEWOBJ + \
            MEMOIZE + POP + \
        gen_stack_global('builtins', 'list') + \
            gen_stack_global('builtins', 'str.encode') + \
                gen_stack_global('builtins', 'print') + \
                    UNICODE + b"What's the flag? \n" + \
                    TUPLE1 + \
                REDUCE + POP + \
                gen_stack_global('builtins', 'input') + \
                    UNICODE + b'> \n' + \
                    TUPLE1 + \
                REDUCE + \
                TUPLE1 + \
            REDUCE + \
            TUPLE1 + \
        REDUCE + MEMOIZE + POP + \
        gen_stack_global('random', 'seed') + \
            UNICODE + b'five nights as freddy\n' + \
            TUPLE1 + \
        REDUCE + POP +\
        gen_stack_global('random', 'shuffle') + \
            GET + b'1\n' + \
            TUPLE1 + \
        REDUCE + POP + \
        gen_stack_global('builtins', 'list') + \
            gen_stack_global('builtins', 'map') + \
                gen_stack_global('builtins', 'int.__xor__') + \
                gen_stack_global('random', 'randbytes') + \
                    gen_stack_global('builtins', 'len') + \
                        GET + b'1\n' + \
                        TUPLE1 + \
                    REDUCE + \
                    TUPLE1 + \
                REDUCE + \
                GET + b'1\n' + \
                TUPLE3 + \
            REDUCE + \
            TUPLE1 + \
        REDUCE + MEMOIZE + POP + \
        gen_stack_global('builtins', 'any') + \
            gen_stack_global('builtins', 'map') + \
                gen_stack_global('builtins', 'int.__xor__') + \
                enc_flag_pickle + \
                GET + b'2\n' + \
                TUPLE3 + \
            REDUCE + \
            TUPLE1 + \
        REDUCE + MEMOIZE + POP + \
        gen_stack_global('builtins', 'int.__or__') + \
            GET + b'3\n' + \
            gen_stack_global('builtins', 'int.__ne__') + \
                gen_stack_global('builtins', 'len') + \
                    GET + b'2\n' + \
                    TUPLE1 + \
                REDUCE + \
                INT + b'59\n' + \
                TUPLE2 + \
            REDUCE + \
            TUPLE2 + \
        REDUCE + MEMOIZE + POP + \
        gen_stack_global('builtins', 'list.__getitem__') + \
            MARK + \
                UNICODE + b'Looks like you got it!\n' + \
                UNICODE + b'Nah, try again.\n' + \
            LIST + \
            GET + b'4\n' + \
            TUPLE2 + \
        REDUCE + \
        STOP

print(payload)
# pickletools.dis(payload)
print(loads(payload))


