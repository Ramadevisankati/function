def diff(l):
    i=0
    a=l[i+1]-l[i]
    while i<len(l)-1:
        if l[i+1]-l[i]==a:
            print("True")
        else:
            print("False")
        i=i+1
li=[3,6,9,12,15,18,21]
diff(li)
