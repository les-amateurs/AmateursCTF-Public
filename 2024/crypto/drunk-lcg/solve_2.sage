for i,j in zip(values, org):
    assert i ^^ xor == j
    A = Matrix([[i, 0, 2^360, 1], [bm, 0, 1, 0], [small, 2^180, 0, 0]])
    a = A.LLL()
    assert a[-1][-1] == 1
    try:
        print(bytes.fromhex(hex((-a[-1][0] + i)^^j)[2:]))
    except:
        print("BAD")