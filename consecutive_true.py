def diff(l):
    i=0
    while i<=len(l)-2:
        if l[i+1]-l[i]==1:
            print("True")
        else:
            print("False")
        i=i+1
diff([1,2,3,4,5,9])
