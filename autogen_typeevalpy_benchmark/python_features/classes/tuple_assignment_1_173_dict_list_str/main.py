# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'xwjpo': 11, 'cuqfp': 11, 'xzqns': 12}

    def func2(self):
        return [84, 10, 37]

    def func3(self):
        return 'nsasu'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
