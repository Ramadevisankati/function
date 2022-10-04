def string(s):
    upper=0
    lower=0
    i=0
    while i<len(s):
        if s[i].isupper():
            upper=upper+1
    
        elif s[i].islower():
            lower=lower+1
        i=i+1
    return upper
    return lower
    
s='The quick Brow Fox'
print(string(s))