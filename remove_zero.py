def my_num(a):
    i=0
    l=str(a)
    while i<len(l):
        if l[i]!="0":
            print(l[i],end="")
        i=i+1
n=int(input("enter the number: "))
my_num(n)