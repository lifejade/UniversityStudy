import math

def gcd(a,b):
    if a > b:
        tmp = a
        a = b
        b = tmp
    #a < b
    if a ==0:
        return b
    if b % a == 0:
        return a
    else:
        return gcd(b % a, a)



def pollard_rho(n):
    def g(x,n):
        return (x*x + 1) % n;

    x = 2
    y = 2
    d = 1
    while  d == 1:
        x = g(x,n)
        y = g(g(y,n),n)
        d = gcd(abs(x-y),n)

    if 1 < d < n:
        return d
    else:
        return -1

while True:
    n = int(input())
    if pollard_rho(n) == -1:
        print("has no factor")
        continue
    print("factor: ",pollard_rho(n))
    print("remainder : ",int(n/pollard_rho(n)))
    if n == -1:
        break
