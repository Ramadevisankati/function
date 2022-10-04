def vote(a):
    if a>=18:
        print("eligible to vote")
    else:
        print("not eligible to vote")
n=int(input("enter the number: "))
vote(n)