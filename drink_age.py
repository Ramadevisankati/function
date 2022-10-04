def drink(age):
    if age <=14:
        return "toddy"
    elif age <18:
        return "coke"
    elif age==18:
        return "beer"
    elif age>=21:
        return "whisky"
n=int(input("enter the number: "))
print(drink(n))