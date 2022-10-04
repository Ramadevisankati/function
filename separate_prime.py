# l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
# i=1
# count=0
# li=[]
# while i<len(l):
#     if l[i]%i==0:
#         print(l[i])
    # else:
    #     print(l[i])
        # i=i+1 

def diff_Prime():
    l1 = int(input("enter the number: "))
    li = int(input("enter the number: "))
    l=[]
    for num in range(l1, li + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                l.append(num)
    print(l)
diff_Prime()
           