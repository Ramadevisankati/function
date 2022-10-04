def function1(a):
    print(a)
    def function2(b):
        c=10
        return a*b*c
    def function3():
        def function4():
            print(function2(10))
        function4()
    function3()
    print(function2(10))
function1(5)

    