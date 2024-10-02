with open('runtime/output.txt', 'w+') as __import__('sys').stdout:
        program = 'try:a092d5a343d2b5a7b297b2d543d2a3b5a78247e6962707b3d513d2a3a3b592825646f6365646e292d5a35313b59782875686d6f62766e292825646f636e656e297d3a7b3d513d2a3a3b556d616e6e256d397a35602371602e6f69647075636875402470756368756a0a3972747pyquinejailgolf\nexcept Exception as e:y=e.name[::-1];z=y.encode().fromhex(y[15:]).decode()[::-1];print(z[:-4]+y+z[-4:])\n\n'
        safe_builtins = {}
        for i in dir(__builtins__):
            if i[0] not in __import__('string').ascii_lowercase:
                safe_builtins[i] = eval(i)
        safe_builtins['print'] = print
        new_builtins = {'__builtins__':safe_builtins}
        try:exec(program, new_builtins, new_builtins)
        except:pass