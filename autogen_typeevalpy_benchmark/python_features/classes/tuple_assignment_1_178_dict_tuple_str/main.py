# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'kyliw': 80, 'ruiea': 66, 'kblmb': 19}

    def func2(self):
        return (27, 7, 62)

    def func3(self):
        return 'rabfw'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
