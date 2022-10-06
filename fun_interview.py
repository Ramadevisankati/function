# def multiple():
#     n=int(input("enter the num: "))
#     m=int(input("enter the num: "))
#     i=0
#     while i<=m:
#         if i%n==0:
#             print(i)
#         i=i+1
# multiple()

# a=[2,4,[4,3],[8,1]]
# def sum(a):
#     i=0
#     for num in a:
#         if type(num)==list:
#             i=i+sum(num)
#         else:
#             i=i+num
#     return i
# print(sum([2,4,[4,3],[8,1]]))

#fibonacci 
def fibonacci(a):
    if a<=1:
        return a
    else:
        return (fibonacci(a-1))+fibonacci(a-2)
n=int(input("enter the num: "))
if n>0:
    i=0
    while i<=n:
        print(fibonacci(i))
        if i>6:
            break
        i=i+1


# print(fibonacci(10))

