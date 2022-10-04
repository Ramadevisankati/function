def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def floor(a,b):
    return a//b
a=5
b=9
o=input("enter the value: ")
if o=="+":
    print(add(a,b))
elif o=="*":
    print(multiply(a,b))
elif o=="//":
    print(floor(a,b))
else:
    print("wrong attempt")
