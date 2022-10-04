def showNumber(limit):
    i=0
    while i<=limit: 
        print(i,end=" ") 
        if(i%2==0):
            print("EVEN") 
        else:
            print("ODD") 
        i=i+1
limit=int(input("Enter limit:"))
showNumber(limit)