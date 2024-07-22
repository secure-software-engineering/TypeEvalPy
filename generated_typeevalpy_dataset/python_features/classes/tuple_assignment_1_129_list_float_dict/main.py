# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [64, 36, 28]

    def func2(self):
        return 58.73

    def func3(self):
        return {'hvyrz': 23, 'uxhly': 8, 'gypnl': 27}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
