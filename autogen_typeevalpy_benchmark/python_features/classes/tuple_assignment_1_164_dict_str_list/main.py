# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'ahkwg': 75, 'mnftn': 78, 'lekhx': 19}

    def func2(self):
        return 'wkdlb'

    def func3(self):
        return [25, 68, 6]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
