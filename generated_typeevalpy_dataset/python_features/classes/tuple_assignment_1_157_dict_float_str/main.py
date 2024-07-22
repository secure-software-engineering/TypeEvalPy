# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'jgnpv': 75, 'hidgd': 81, 'scakx': 85}

    def func2(self):
        return 50.6

    def func3(self):
        return 'fzbwa'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
