# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [53, 19, 86]

    def func2(self):
        return {'tiukj': 15, 'jjpzg': 16, 'tlfml': 1}

    def func3(self):
        return 28.26


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
