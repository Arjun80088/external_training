def fact(k,r):
    if k==1:
        return r
    r =r*k
    return fact(k-1,r)
k=int(input())
r=1
print(fact(k,r))

