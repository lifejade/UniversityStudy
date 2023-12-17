from fractions import Fraction


def add_points(P, Q):
    if P == Q:
        s = Fraction((3 * P[0] ** 2), (2 * P[1]))
    else:
        s = Fraction((Q[1] - P[1]), (Q[0] - P[0]))
    
    x3 = s**2 - P[0] - Q[0]
    y3 = s * (x3 - P[0]) + P[1]
    y3 *= -1
    return x3, y3

def mult_points(P,m):
    if(m == 1):
        return P
    if(m == 2):
        return add_points(P,P)
    
    mbit1 = m % 2;
    m=m>>1
    if mbit1 == 1:
        return add_points(P, mult_points(mult_points(P,m), 2))
    else:
        return mult_points(mult_points(P,m), 2);

P = (3, 5)
P4 = mult_points(P,4)
print("4P =", P4[0], ", ", P4[1])
