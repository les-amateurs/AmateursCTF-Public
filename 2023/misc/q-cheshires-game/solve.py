from base64 import b64encode
from qiskit import QuantumCircuit
import numpy as np
pi = np.pi

# see https://learn.qiskit.org/course/basics/entanglement-in-action#entanglement-30-42
# very basic implementation here

# alice_x_0
alice_x_0 = QuantumCircuit(2, 1)
alice_x_0.cx(0, 1)
alice_x_0.h(0)

# alice_x_1
alice_x_1 = QuantumCircuit(2, 1)
alice_x_1.cx(0, 1)
alice_x_1.h(0)
alice_x_1.x(0)

# bob_y_0
bob_y_0 = QuantumCircuit(2, 1)
bob_y_0.cx(0, 1)

# bob_y_1
bob_y_1 = QuantumCircuit(2, 1)



strategies = [alice_x_0, alice_x_1, bob_y_0, bob_y_1]
strategies = [b64encode(qc.qasm().encode()) for qc in strategies]

# send strategies to server
from pwn import remote
import subprocess
r = remote('amt.rs', 31011)

def solvePOW():
    pow = r.recvline().decode().strip().split(': ')[1]
    print(pow)
    res = subprocess.check_output(['bash', '-c', pow]).strip()
    print(res)
    r.sendline(res)
solvePOW()

for strategy in strategies:
    r.sendline(strategy)

flag = r.recvall().decode().strip()
flag = flag.split('\n')[-1]
print(flag)
