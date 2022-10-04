def string_reverse(a):
    b = ''
    length= len(a)
    while length > 0:
        b += a[length - 1 ]
        length= length- 1
    return b
print(string_reverse("'1234abcd'"))