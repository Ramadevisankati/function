def prime():
    a=int(input("enter the number: "))
    c=0
    i=1
    while i<=a:
        if a%i==0:
            c=c+1
        i=i+1
    if c==2:
        print("it is prime number")
    else:
        print("it is not a prime")
prime()