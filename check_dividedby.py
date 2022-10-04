def is_divide_by(a,b,c):
    if a//c==b:
        return "True"
    else:
        return "False"
l=int(input("enter the number: "))
l2=int(input("enter the number: "))
l3=int(input("enter the number: "))
print(is_divide_by(l,l2,l3))

        