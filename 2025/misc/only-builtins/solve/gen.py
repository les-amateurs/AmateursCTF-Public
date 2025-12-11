# for i in range(ord('d'), ord('s')):
#     print(f"__auto_type v{i+2000}=__builtin_strcat(v5,v3);",end='')

for i in range(32):
    j = i*3 + 300
    print(f'__auto_type v{j}=__builtin_scanf(v3102,v500);__auto_type v{j+1}=__builtin_scanf(v5,v3);__auto_type v{j+2}=__builtin_printf(v3);', end='')
