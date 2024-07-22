# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 50

    def func2(self):
        return {'gtlok': 4, 'zmefb': 57, 'sxcju': 10}

    def func3(self):
        return (64, 40, 64)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
