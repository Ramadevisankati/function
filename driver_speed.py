def speed(s):
    if s<=70:
        print("OK")
    elif s>70:
        points=(s-70)//5
        if points<=12:
            print("points",points)
        else:
            print("licence suspended")
n=int(input("enter the number:"))
speed(n)
        