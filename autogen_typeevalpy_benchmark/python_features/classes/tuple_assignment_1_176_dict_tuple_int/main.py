# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'wshcz': 63, 'slzvh': 71, 'mpcma': 66}

    def func2(self):
        return (87, 21, 41)

    def func3(self):
        return 25


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
