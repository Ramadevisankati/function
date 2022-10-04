def unique(l):
    i=0
    l2=[]
    while i<len(l):
        if l[i] not in l2:
            l2.append(l[i])
        i=i+1
    return l2
# l=[1,2,3,3,3,3,4,5]
print(unique([1,2,3,3,3,3,4,5]))
