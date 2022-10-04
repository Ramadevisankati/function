l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
name="Ramadevi"
a=[]
i=0
while i<len(name):
    j=0
    while j<len(l):
        if name[i]==l[j]:
            a.append(j)
        j=j+1
    i=i+1
print(a)
