import random
from delta_patch import apply_patch_to_buffer
from ctypes import (windll, wintypes, c_uint64, cast, POINTER, Union, c_ubyte,
                    LittleEndianStructure, byref, c_size_t, c_uint32,)
from Crypto.Util.strxor import strxor

DELTA_FLAG_TYPE = c_uint64
DELTA_FLAG_NONE = 0x00000000
DELTA_FILE_TYPE = c_uint64
DELTA_FILE_NONE = 0x00000001
HEADER = b'PA30XXXXXXXX\x18#'  # 14 bytes

class DELTA_HASH(LittleEndianStructure):
    _fields_ = [
        ('HashSize', c_uint32),
        ('HashValue', c_ubyte * 32)
    ]

class DELTA_INPUT(LittleEndianStructure):
    class U1(Union):
        _fields_ = [('lpcStart', wintypes.LPVOID),
                    ('lpStart', wintypes.LPVOID)]
    _anonymous_ = ('u1',)
    _fields_ = [('u1', U1),
                ('uSize', c_size_t),
                ('Editable', wintypes.BOOL)]


class DELTA_OUTPUT(LittleEndianStructure):
    _fields_ = [('lpStart', wintypes.LPVOID),
                ('uSize', c_size_t)]


class DELTA_HEADER_INFO(LittleEndianStructure):
    _fields_ = [('FileTypeSet', DELTA_FILE_TYPE),
                ('FileType', DELTA_FILE_TYPE),
                ('Flags', DELTA_FLAG_TYPE),
                ('TargetSize', c_size_t),
                ('TargetFileTime', wintypes._FILETIME),
                ('TargetHashAlgId', c_uint32),
                ('TargetHash', DELTA_HASH)]


CreateDelta = windll.msdelta.CreateDeltaB
CreateDelta.argtypes = [DELTA_FILE_TYPE, DELTA_FLAG_TYPE, DELTA_FLAG_TYPE, DELTA_INPUT, DELTA_INPUT,
                        DELTA_INPUT, DELTA_INPUT, DELTA_INPUT, POINTER(None), DELTA_FLAG_TYPE, POINTER(DELTA_OUTPUT)]
CreateDelta.rettype = wintypes.BOOL

GetDeltaInfoB = windll.msdelta.GetDeltaInfoB
GetDeltaInfoB.argtypes = [DELTA_INPUT, POINTER(DELTA_HEADER_INFO)]
GetDeltaInfoB.rettype = wintypes.BOOL

DeltaFree = windll.msdelta.DeltaFree
DeltaFree.argtypes = [wintypes.LPVOID]
DeltaFree.rettype = wintypes.BOOL
gle = windll.kernel32.GetLastError


# call
def createdelta(buf, final):
    dd = DELTA_INPUT()
    ds = DELTA_INPUT()
    dout = DELTA_OUTPUT()
    options = DELTA_INPUT()
    globaloptions = DELTA_INPUT()

    options.lpStart = cast(None, wintypes.LPVOID)
    options.Editable = False
    options.uSize = 0
    globaloptions.lpStart = cast(None, wintypes.LPVOID)
    globaloptions.uSize = 0

    ds.lpcStart = cast(buf, wintypes.LPVOID)
    ds.uSize = len(buf)
    ds.Editable = False

    dd.lpcStart = cast(final, wintypes.LPVOID)
    dd.uSize = len(final)
    dd.Editable = False

    args = [
        DELTA_FILE_NONE,
        DELTA_FLAG_NONE,
        DELTA_FLAG_NONE,
        ds,
        dd,
        options,
        options,
        globaloptions,
        cast(None, wintypes.LPVOID),
        0x8004,
        # 0x0,
        byref(dout)
    ]

    status = CreateDelta(*args)
    if status == 0:
        raise Exception("CreateDelta failed with error {}".format(gle()))

    return dout
    # buf, n = dout.lpStart, dout.uSize

    # # first 14 bytes seem to be useless?
    # outbuf = bytes((c_ubyte*n).from_address(buf))
    # return (outbuf, len(outbuf))

def get_patch_info(_delta):
    delta = DELTA_INPUT()
    delta.lpcStart = cast(_delta, wintypes.LPVOID)
    delta.uSize = len(_delta)
    delta.Editable = False

    header_out = DELTA_HEADER_INFO()

    if GetDeltaInfoB(delta, header_out):
        return [header_out.FileTypeSet,
        header_out.FileType,
        header_out.Flags,
        header_out.TargetSize,
        header_out.TargetFileTime.dwLowDateTime,
        header_out.TargetFileTime.dwHighDateTime,
        hex(header_out.TargetHashAlgId),
        header_out.TargetHash.HashSize,
        bytes(header_out.TargetHash.HashValue[:header_out.TargetHash.HashSize])]
    else:
        return "Failed to run GetDeltaInfoB"
    
def remove_hash(delta, sz):
    _, _, _, _, _, _, hashalg, hashsize, _ = get_patch_info(delta)
    print(hashalg, hashsize)
    header = delta[:14] + sz # 256 size
    return header + delta[16 + 4 + hashsize:]

def gen_rand(vals=b'01', sz=256):
    buf = [vals[round(random.random())] for r in range(sz)]
    return bytes(buf)

def print_header(header_out):
    print(f'{header_out.FileTypeSet=}')
    print(f'{header_out.FileType=}')
    print(f'{header_out.Flags=}')
    print(f'{header_out.TargetSize=}')
    print(f'{header_out.TargetFileTime.dwLowDateTime=}')
    print(f'{header_out.TargetFileTime.dwHighDateTime=}')
    print(f'{hex(header_out.TargetHashAlgId)=}')
    print(f'{header_out.TargetHash.HashSize=}')
    print(f'{bytes(header_out.TargetHash.HashValue[:header_out.TargetHash.HashSize]).hex()=}')

if __name__ == '__main__':

    buf =   b'amateursCTF{FAKE_FLAG_BTW_DONT_SUBMIT_THIS_PLEASE_THX}'
    final = b'amateursCTF{suff3r_th3_p41n_of_a_m1ll10n_wind0ws_d3v5}'
    print(buf, final, sep='\n')
    out1 = createdelta(buf, final)
    outbuf = bytes((c_ubyte*out1.uSize).from_address(out1.lpStart))
    print(outbuf, len(outbuf))
    print('\\x' + '\\x'.join(f'{i:02x}' for i in outbuf))

    delta = DELTA_INPUT()
    delta.lpcStart = cast(outbuf, wintypes.LPVOID)
    delta.uSize = len(outbuf)
    delta.Editable = False

    header_out = DELTA_HEADER_INFO()

    if GetDeltaInfoB(delta, header_out):
        print_header(header_out)

    buf = b'amateursCTF{fake_flag_btw_dont_submit_this_please_thx}'
    out = apply_patch_to_buffer(buf, outbuf)
    print(out)