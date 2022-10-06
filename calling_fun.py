def all_num():
    i=1
    a=[]
    while i<=20:
        a.append(i)
        i=i+1
    return a
def even_num():
    arr=all_num()
    i=0
    b=[]
    c=[]
    while i<len(arr):
        if arr[i]%2==0:
            b.append(arr[i])
        else:
            c.append(arr[i])
        i=i+1
    print(arr)
    print(b)
    print(c)
even_num()


