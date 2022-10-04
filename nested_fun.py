def outer():
    print("this is outer function")
    def inner():
        print("this is inner function")
    inner()
outer()