def counting():
    a=["naga","liki","laxmi","rama"]
    i=0
    l=[]
    l2=[]
    while i<len(a):
        if len(a[i])%2==0:
            l.append(a[i])
        else:
            l2.append(a[i])
        i=i+1
    print(l)
    print(l2)
counting()
