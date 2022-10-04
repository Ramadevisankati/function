def num(list1):
    pos_count=0
    neg_count = 0
    for num in list1:
        if num >0:
            pos_count += 1
        else:
            neg_count += 1
    print("Positive numbers in the list: ", pos_count)
    print("Negative numbers in the list: ", neg_count)
num(list1 = [2, -7, 5, -64, -14])