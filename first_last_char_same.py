def my_char(l):
    i=0
    count=0
    while i<len(l):
        if l[i][0]==l[i][-1]:
            count+=1
        i=i+1
    print(count)
my_char(l=['abc','xyz','aba','1221','assa'])

