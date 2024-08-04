# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (45, 97, 15)

    def func2(self):
        return {'snaxx': 55, 'oehjl': 63, 'cqxmb': 17}

    def func3(self):
        return [89, 12, 78]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
