def pow_mod(a,e,m):
    if(e == 1):
        return a % m;
    ebit1 = e % 2;
    e=e>>1
    return (a**ebit1 % m) * ((pow_mod(a,e,m)**2) % m) % m;


n=int(input())

if(n%2==0):
    print("ERROR, n must be odd")
    exit(0)

tmp = n - 1
k=0
while(tmp % 2 == 0):
    k+=1
    tmp = tmp >> 1
q = tmp


isComposite = False
for a in range(1,n):
    if(pow_mod(a,q,n) == 1):
        continue
    
    check2 = True
    for i in range(0,k):
        if(pow_mod(a,q*(2**i),n)==n-1):
            check2 = False
            break
    if(not check2):
        continue
    
    isComposite = True
    break

if isComposite:
    print("n is composite number")
else :
    print("n is not composite number")
