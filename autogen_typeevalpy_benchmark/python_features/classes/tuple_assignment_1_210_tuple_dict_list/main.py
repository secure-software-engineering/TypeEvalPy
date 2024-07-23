# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (88, 43, 14)

    def func2(self):
        return {'lmayq': 78, 'duunl': 67, 'edvgr': 76}

    def func3(self):
        return [89, 16, 91]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
