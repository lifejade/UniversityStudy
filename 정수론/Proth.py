def pow_mod(a,e,m):
    if(e == 1):
        return a % m;
    ebit1 = e % 2;
    e=e>>1
    return (a**ebit1 % m) * ((pow_mod(a,e,m)**2) % m) % m;

n = 1038337
e = int((n - 1)/2)
for i in range(1,n):
    if pow_mod(i,e,n) == n-1:
        print("a : ",i)
        print(n, "is prime")
        exit(0)

print(n, " is not prime")
