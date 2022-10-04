def even():
    i=1
    a=[]
    while i<=10:
        a.append(i)
        i=i+1
    print(a)
even()
def xyz():
    even()
    i=1
    b=[]
    c=[]
    while i<=10:
        if i%2==0:
            b.append(i)
        else:
            c.append(i)
        i=i+1
    print(b)
    print(c)
xyz()