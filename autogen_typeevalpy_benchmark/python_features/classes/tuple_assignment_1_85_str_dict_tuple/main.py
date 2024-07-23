# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 'pmmrj'

    def func2(self):
        return {'mfskh': 100, 'uwgsh': 44, 'yqiry': 40}

    def func3(self):
        return (2, 100, 95)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
