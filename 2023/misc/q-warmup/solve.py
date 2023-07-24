enc = b'\xbe\xb6\xbeXF\xa6\\\xa2\x82\x98\x84R\xb4 X\xb0N\xb4\xbaj^f\xd8\xb4X\xa6\xb6j\xd8\xbc \xa6XjX\xb0\xde\xa2j\xd8Xj~HHV' 
msg = b''

# from qiskit import QuantumCircuit
# from qiskit import Aer, execute
# backend = Aer.get_backend('qasm_simulator')
# def encode_quantum(bits):
#     circuit = QuantumCircuit(8, 8)
#     for i, bit in enumerate(bits):
#         if bit == '1':
#             circuit.x(i)
        
#     for i in range(7, 0, -1):
#         circuit.cx(i, i-1)
    
#     circuit.measure(range(8), range(8))
#     job = execute(circuit, backend, shots=1)
#     result = job.result()
#     result = list(result.get_counts().keys())[0][::-1]

#     ret = int(bits, 2) ^ int(result, 2)
#     return ret

def encode_classic(bits):
    ret = [int(bit) for bit in bits]
    for i in range(7, 0, -1):
        ret[i-1] ^= ret[i]
    
    ret = ''.join([str(bit) for bit in ret])
    ret = int(bits, 2) ^ int(ret, 2)
    return ret


import string

enc_map = {encode_classic(bin(i)[2:].zfill(8)): i for i in string.printable.encode()}
print(enc_map)

for i in enc:
    msg += bytes([enc_map[i]])

print(msg)