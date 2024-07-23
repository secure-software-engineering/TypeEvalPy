# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 'jryul'

    def func2(self):
        return {'pirau': 79, 'fxbnw': 98, 'ztgty': 68}

    def func3(self):
        return 79


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
