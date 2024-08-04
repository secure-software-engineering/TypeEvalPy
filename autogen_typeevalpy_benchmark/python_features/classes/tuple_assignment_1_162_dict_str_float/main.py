# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'ocsgz': 62, 'aibyj': 36, 'cxjri': 2}

    def func2(self):
        return 'oedkm'

    def func3(self):
        return 32.28


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
