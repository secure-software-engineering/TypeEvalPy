# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'wdpmr': 54, 'haibq': 2, 'snqtx': 71}

    def func2(self):
        return 'mwkwq'

    def func3(self):
        return (93, 73, 96)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
