# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (42, 33, 65)

    def func2(self):
        return [43, 49, 20]

    def func3(self):
        return {'ijvei': 34, 'wtkwr': 14, 'rkcsm': 95}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
