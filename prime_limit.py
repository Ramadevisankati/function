def prime_interval():
    n=1
    while n<=100:
        i=2
        while i<=n//2:
            if n%i==0:
                break
            i=i+1
        if i>n//2:
            print(n,end=" ")
        n+=1
prime_interval()