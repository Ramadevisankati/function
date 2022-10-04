a="MyNAmeiSrAma"
i=0
c=0
s=0
while i<len(a):
    b=a[i]
    if b.isupper():
        c+=1
    else:
        s+=1
    i=i+1
print("Capital",c)
print("Small",s)
