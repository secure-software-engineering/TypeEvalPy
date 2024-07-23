# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 'rohfv'

    def func2(self):
        return (94, 72, 13)

    def func3(self):
        return {'exjld': 14, 'hyiwl': 88, 'yjnlv': 29}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
