# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 22.73

    def func2(self):
        return {'qnglk': 38, 'amomv': 36, 'yzutr': 47}

    def func3(self):
        return True


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
