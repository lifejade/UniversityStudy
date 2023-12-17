def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception('역원이 존재하지 않습니다.')
    else:
        
        return x % m

def mod_inverse_b(a,m):
    return a**(m-2) % m;
    
def add_points(P, Q,mod):
    if P == Q:
        s = (3 * P[0] ** 2 - 4) * mod_inverse_b(2 * P[1],mod) % mod
    else:
        s = (Q[1] - P[1]) * mod_inverse_b(Q[0] - P[0],mod) % mod
    
    x3 = s**2 - P[0] - Q[0]
    y3 = s * (x3 - P[0]) + P[1]
    y3 *= -1
    x3 %= mod
    y3 %= mod
    return x3, y3

def mult_points(P,m,mod):
    if(m == 1):
        return P
    if(m == 2):
        return add_points(P,P, mod)
    
    mbit1 = m % 2;
    m=m>>1
    if mbit1 == 1:
        return add_points(P, mult_points(mult_points(P,m,mod), 2, mod),mod)
    else:
        return mult_points(mult_points(P,m, mod), 2,mod);

P = (2, 2)
mod = 1013

print(mod_inverse_b(2,5))
print("100P =", mult_points(P,100, mod))
