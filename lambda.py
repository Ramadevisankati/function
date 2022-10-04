myfun=lambda x:x*3
b=myfun(5)
print(b)

# Program to filter out only the even items from a list
# my_list = [1, 5, 4, 6, 8, 11, 3, 12]

# new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# print(new_list)


my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)