def even_odd():
    i=0
    n=int(input("enter the number: "))
    while i<=n:
        num=int(input("enter the number: "))
        if num%2==0:
            return num*100
        else:
            return num*-1
        i=i+1
print(even_odd())