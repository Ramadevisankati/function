#positional argument
def display(a,b):
    print(a,b)
display(10,20)

#keyword argument
def display(a,b):
    print(a,b)
display(b=20,a=10)

#default argument
def display(name,age=20):
    print(name)
    print(age)
display(name="rama",age=23)
display(name="ramadevi")

# *arbitrary arguments
def add(*a):
    for i in a:
        total=0
        total=total+i
    print(total)
add(10,20,30,50)