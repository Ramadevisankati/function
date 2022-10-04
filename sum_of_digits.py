def digits(l):
    i=0
    j=0
    l2=[]
    while i<len(l):
        a=l[i]%10
        b=l[i]//10
        i=i+1
        c=a+b
        l2.append(c)
    print(l2)
digits([12, 67, 98, 34])