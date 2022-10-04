num =int(input("enter the num: "))
def even_odd(num):
    if num==0:
        print(num,"is neither odd nor even")
    elif num%2==0:
        print(num,"is an even number")
    elif num%2!=0:
        print(num,"is an odd numer")
even_odd(num)