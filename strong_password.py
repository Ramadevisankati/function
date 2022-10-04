def password_check():
    a=0
    b=0
    c=0
    d=0
    n=input("enter the password: ")
    if len(n)>=6:
        for i in n:
            if (i.islower()):
                a=a+1
            if (i.isupper()):
                b=b+1
            if (i.isdigit()):
                c=c+1
            if (i=="*",i=="@",i=="$",i==".",i=="%",i=="-",i=="#",i==","):
                d=d+1
        if (a>=1 and b>=1 and c>=1 and d>=1 and a+b+c+d>=len(n)):
            print("strong password")
        else:
            print("weak password")
password_check()
            