#!/usr/bin/env sage

# llm script because im lazy

o = """1471207943545852478106618608447716459893047706734102352763789322304413594294954078951854930241394509747415
1598692736073482992170952603470306867921209728727115430390864029776876148087638761351349854291345381739153
7263027854980708582516705896838975362413360736887495919458129587084263748979742208194554859835570092536173
1421793811298953348672614691847135074360107904034360298926919347912881575026291936258693160494676689549954
7461500488401740536173753018264993398650307817555091262529778478859878439497126612121005384358955488744365
7993378969370214846258034508475124464164228761748258400865971489460388035990421363365750583336003815658573""".splitlines()

for i,j in enumerate(o,1):
    exec(f'o_{i} = Integer(j)')

print("[*] Starting algebraic attack (Resultant GCD method)...")

# 1. Setup the Polynomial Ring over Integers
P_ZZ.<x> = PolynomialRing(ZZ)

# 2. Define the geometric series polynomials A_n(x)
# A_n(x) = x^(n-1) + ... + x + 1
A_3 = x**2 + x + 1
A_4 = x**3 + x**2 + x + 1
A_5 = x**4 + x**3 + x**2 + x + 1
A_6 = x**5 + x**4 + x**3 + x**2 + x + 1

# 3. Create the three polynomials P_A, P_B, P_C
# P_A comes from o_3, o_4
P_A = (o_3 - x**3 * o_2) * A_4 - (o_4 - x**4 * o_3) * A_3

# P_B comes from o_4, o_5
P_B = (o_4 - x**4 * o_3) * A_5 - (o_5 - x**5 * o_4) * A_4

# P_C comes from o_5, o_6
P_C = (o_5 - x**5 * o_4) * A_6 - (o_6 - x**6 * o_5) * A_5

print("[*] Constructed P_A(x), P_B(x), and P_C(x).")

# 4. Compute the two resultants. These are large integers.
# R_1 = Res(P_A, P_B) = K_1 * m
print("[*] Computing Resultant 1...")
R_1 = P_A.resultant(P_B, x)

# R_2 = Res(P_B, P_C) = K_2 * m
print("[*] Computing Resultant 2...")
R_2 = P_B.resultant(P_C, x)

# 5. Compute the GCD of the two resultants to find m
# G = gcd(R_1, R_2) = gcd(K_1 * m, K_2 * m) = m * gcd(K_1, K_2)
# Since gcd(K_1, K_2) is almost certainly 1, G should be m.
print("[*] Computing integer GCD of resultants...")
m_candidate = gcd(R_1, R_2)

# In case gcd(K_1, K_2) > 1, m will be the largest prime factor
# of m_candidate. For this problem, we can be quite confident
# m_candidate is m or a small multiple.
m = m_candidate.prime_to_m_part(m_candidate.nbits()) # Extracts prime m

if not m.is_prime():
    print("[-] GCD is not prime. Attack may have failed.")
    # Fallback: check factors of the gcd
    m = m_candidate.factor()[-1][0] # Get largest prime factor
    if not m.is_prime():
        print("[-] Could not isolate m. Exiting.")
        exit(1)

print(f"[+] Found m: {m}")

# 6. Now that we have m, find 'a'
# 'a' is a common root of P_A and P_B modulo m.
# We find it by computing their GCD in the ring Z_m[x].
P_mod_m.<x_m> = PolynomialRing(Zmod(m))

# Cast the polynomials into the new ring
P_A_mod_m = P_mod_m(P_A)
P_B_mod_m = P_mod_m(P_B)

# Compute the GCD
G = gcd(P_A_mod_m, P_B_mod_m)

# The root of the GCD is 'a'
if G.degree() != 1:
    print("[-] GCD is not linear. Attack failed.")
    exit(1)

a = G.roots(multiplicities=False)[0]
print(f"[+] Found a: {a}")

# 7. Find 'c'
# Use the equation for o_3: c * A_3(a) = o_3 - a^3 * o_2 (mod m)
try:
    inv_A3 = pow(A_3(a), -1, m)
    c = (o_3 - (a**3 * o_2)) * inv_A3 % m
    print(f"[+] Found c: {c}")
except ValueError:
    print("[-] Failed to compute modular inverse for A_3(a).")
    exit(1)

# 8. Find 'flag'
# Use the equation for o_1: o_1 = a * flag + c (mod m)
# -> a * flag = o_1 - c (mod m)
try:
    inv_a = pow(a, -1, m)
    flag_long = (o_1 - c) * inv_a % m
    print(f"[+] Found flag (as integer): {flag_long}")
except ValueError:
    print("[-] Failed to compute modular inverse for a.")
    exit(1)

# 9. Convert flag back to bytes
flag_bytes = print(bytes.fromhex(hex(flag_long)[2:]))
