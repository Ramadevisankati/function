def index_string():
    li="RamADeVi"
    i=0
    l2=[]
    while i<len(li):
        if li[i]==li[i].lower():
            l2.append(i)
        i=i+1
    print(l2)
index_string()
