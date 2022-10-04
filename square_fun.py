def my_sqr():
    i=1
    j=30
    l=[]
    l2=[]
    while i<=5:
        l.append(i*i)
        l2.append(j*j)
        i=i+1
        j=j-1
    list1=l,l2
    print(list1)
my_sqr()