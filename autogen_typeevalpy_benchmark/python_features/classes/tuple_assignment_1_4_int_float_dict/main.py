# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 23

    def func2(self):
        return 50.96

    def func3(self):
        return {'kkbec': 86, 'mpcwt': 2, 'tokcs': 85}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
