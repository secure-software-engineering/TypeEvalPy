# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (65, 92, 86)

    def func2(self):
        return {'tyvfa': 56, 'usgtj': 49, 'msjwo': 39}

    def func3(self):
        return 'fnser'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
