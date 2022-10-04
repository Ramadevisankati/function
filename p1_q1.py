a=['p','q']
i=1
b=[]
while i<=5:
    j=0
    while j<len(a):
        d=a[j]+str(i)
        b.append(d)
        j=j+1
    i=i+1
print(b)
