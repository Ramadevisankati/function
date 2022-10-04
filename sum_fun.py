def sum(a):
    i=0
    sum=0
    while i<len(a):
        sum+=a[i]
        i=i+1
    return sum
print(sum([8,2,3,0,7]))