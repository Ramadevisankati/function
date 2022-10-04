def power(p):
    i=0
    l=[]
    while i<=p:
        a=2**i
        l.append(a)
        i=i+1
    print(l)
n=int(input("enter the number: "))
power(n)