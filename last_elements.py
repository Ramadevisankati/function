def elements(a):
    i=0
    n=int(input("enter the number: "))
    while i<len(a):
        lst=a[-n:]
        print(lst)
        i=i+1
        break
elements(['a',1,'2', 5,'b','q'])
