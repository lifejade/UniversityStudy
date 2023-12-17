y2=0
p = 11
for x in range(0,p):
    y2 = (x**3 + 7) % p
    if(y2 == 0):
        print(x, " : ",0)
        continue;
    
    l=int(y2**((p-1)/2)) % p
    if(l > p/2):
        l=l-p
    print(x, " : ",l)
