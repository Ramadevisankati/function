def fizz_buzz(a):
    if a%3==0 and a%5==0:
        return "Fizz Buzz"
    elif a%3==0:
        return "Fizz"
    elif a%5==0:
        return "Buzz"
    else:
        return a
n=int(input("enter the number: "))
print(fizz_buzz(n))
