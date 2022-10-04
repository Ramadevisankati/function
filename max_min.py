def max_min(li):
    c=0
    i=0
    l2=[]
    a=max(li)
    while i<=len(li):
        c+=1
        l2.append(a)
        l2.append(c)
    print(l2)
max_min([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])