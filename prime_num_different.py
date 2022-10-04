def num():
  i=1
  while i<=15:
        j=2
        count=0
        while j<i:
          if i%j==0:
            count+=1
          j=j+1
        if count==0:
          print("@")
        else:
          print(j)
        i=i+1
num()
