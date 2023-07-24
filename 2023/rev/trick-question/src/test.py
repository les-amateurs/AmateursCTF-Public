flag = "amateursCTF{PY7h0ns_ar3_4_f4m1lY_0f_N0Nv3nom0us_Sn4kes}"
import base64

print(base64.b64encode(open("secret.py", "rb").read().replace(b"\r\n", b"\n")))