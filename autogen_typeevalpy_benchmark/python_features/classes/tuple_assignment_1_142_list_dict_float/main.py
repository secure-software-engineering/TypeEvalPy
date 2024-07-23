# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [27, 52, 41]

    def func2(self):
        return {'himqz': 13, 'mgbmg': 42, 'mbyyl': 27}

    def func3(self):
        return 56.08


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
