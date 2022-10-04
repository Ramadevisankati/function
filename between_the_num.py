def multiples(limit):
    i=0
    while i<=limit:
        if i%3==0 or i%5==0:
            print(i,end=" ")
        i=i+1
multiples(20)