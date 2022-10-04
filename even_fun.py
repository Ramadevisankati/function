def even(a):
    i=0
    l=[]
    while i<len(a):
        if a[i]%2==0:
            l.append(a[i])
        i=i+1
    return l
a=[1, 2, 3, 4, 5, 6, 7, 8, 9]        
print(even(a))
