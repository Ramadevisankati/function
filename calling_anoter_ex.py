def greet(person,first_time=False):
    if first_time:
        return "first time for everything,welcome to"+person
    return "Hello"+person
def greet_all(people):
    for person in people:
        print(greet(person,True))
friends=[" bob"," rama"," austin"]
greet_all(friends)

