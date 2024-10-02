from pwn import *

solver = process("./target/release/solve")

server = remote(args.HOST or "localhost", args.PORT or 5000)

queries = int(server.recvline())

log.info(f"{queries = }")
solver.sendline(f"{queries}".encode())

for i in range(queries):
    query = server.recvline().strip()
    solver.sendline(query)
    ans = solver.recvline().strip()
    log.info(f"{ans = }")
    server.sendline(ans)

server.interactive()