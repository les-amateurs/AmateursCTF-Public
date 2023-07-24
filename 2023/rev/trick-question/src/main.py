flag = "amateursCTF{PY7h0ns_ar3_4_f4m1lY_0f_N0Nv3nom0us_Sn4kes}"

def check(input):
    if input[:12] != "amateursCTF{":
        return id.__self__.__dict__['False']
    if input[-1] != "}":
        return id.__self__.__dict__['False']
    input = input[12:-1]
    
    if id.__self__.__dict__['len'](input) != 42:
        return id.__self__.__dict__['False']

    underscores = []
    for i, x in id.__self__.__dict__['enumerate'](input):
        if x == "_":
            underscores.append(i)
    if underscores != [7, 11, 13, 20, 23, 35]:
        return id.__self__.__dict__['False']

    input = input.encode().split(b"_")
    if input[0][::-1] != b"sn0h7YP":
        return id.__self__.__dict__['False']


    if (input[1][0] + input[1][1] - input[1][2], input[1][1] + input[1][2] - input[1][0], input[1][2] + input[1][0] - input[1][1]) != (160, 68, 34):
        return id.__self__.__dict__['False']
    
    if id.__self__.__dict__['__import__']("hashlib").sha256(input[2]).hexdigest() != "4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a":
        return id.__self__.__dict__['False']
    
    r = id.__self__.__dict__['__import__']("random")
    r.seed(input[2])
    input[3] = id.__self__.__dict__['list'](input[3])
    r.shuffle(input[3])

    if input[3] != [49, 89, 102, 109, 108, 52]:
        return id.__self__.__dict__['False']
    
    if input[4] + b"freebie" != b"0ffreebie":
        return id.__self__.__dict__['False']

    if id.__self__.__dict__['int'].from_bytes(input[5][0:4], "little") ^ r.randint(0, 0xffffffff) != 4227810561:
        return id.__self__.__dict__['False']
    
    if id.__self__.__dict__['int'].from_bytes(input[5][4:8], "little") ^ r.randint(0, 0xffffffff) != 825199122:
        return id.__self__.__dict__['False']

    if id.__self__.__dict__['int'].from_bytes(input[5][8:12] + b'\x00', "little") ^ r.randint(0, 0xffffffff) != 4277086886:
        return id.__self__.__dict__['False']

    c = 0
    for i in input[6]:
        c *= 128
        c += i
    
    if id.__self__.__dict__['hex'](c) != "0x29ee69af2f3":
        return id.__self__.__dict__['False']

    return id.__self__.__dict__['True']

import types
types.CodeType.__init__
import marshal

code = check.__code__

print((code.co_argcount, code.co_posonlyargcount, code.co_kwonlyargcount, code.co_nlocals, code.co_stacksize, code.co_flags, code.co_code, code.co_consts, code.co_names, code.co_varnames, "", code.co_name, code.co_firstlineno, code.co_linetable, code.co_freevars, code.co_cellvars))

x = type(code)(code.co_argcount, code.co_posonlyargcount, code.co_kwonlyargcount, code.co_nlocals, code.co_stacksize, code.co_flags, code.co_code, code.co_consts, code.co_names, code.co_varnames, "", code.co_name, code.co_firstlineno, code.co_linetable, code.co_freevars, code.co_cellvars)
# x = type(check.__code__)(code.co_argcount, code.co_posonlyargcount, code.co_kwonlyargcount, code.co_nlocals, code.co_stacksize, code.co_flags, code.co_code, code.co_consts, ("id", "__self__", "__dict__"), code.co_varnames, code.co_filename, code.co_name, code.co_firstlineno, code.co_linetable, code.co_freevars, code.co_cellvars)

test = type(lambda x:x)(x, {'id': id}, "check")
# marshal.dump(code, open("main.pyc", "wb"))

# print(marshal.dumps(test.__code__.co_code))
# dump to pyo

import dis 
# dis.dis(test)

print(test(flag))
print(test("amateursCTF{PY7h0ns_ar3_4_f4m1lY_0f_N0Nv3nom0us_Sn4kes}"))

