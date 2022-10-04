def harshad_num():
    a=int(input("enter the num: "))
    b=a
    r=0
    sum=0
    while b>0:
        r=b%10
        sum=sum+r
        b=b//10
    if a%sum==0:
        print("harshad number")
    else:
        print("not a harshad number")
harshad_num()