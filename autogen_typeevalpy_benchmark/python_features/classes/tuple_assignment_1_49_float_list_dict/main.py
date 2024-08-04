# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 33.88

    def func2(self):
        return [64, 76, 86]

    def func3(self):
        return {'nzdep': 5, 'qabpi': 42, 'jcfij': 94}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
