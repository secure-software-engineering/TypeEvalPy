# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 'wnasn'

    def func2(self):
        return {'algzt': 44, 'ddomt': 36, 'cpbkk': 35}

    def func3(self):
        return 60


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
