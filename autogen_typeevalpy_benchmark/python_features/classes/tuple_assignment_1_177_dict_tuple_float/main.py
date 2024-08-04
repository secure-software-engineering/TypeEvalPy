# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'zuhrb': 63, 'ypkcj': 14, 'mwmnd': 54}

    def func2(self):
        return (37, 73, 9)

    def func3(self):
        return 59.06


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
