# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [53, 2, 64]

    def func2(self):
        return 'ntkjn'

    def func3(self):
        return {'gumbs': 85, 'saboe': 61, 'qmyzu': 65}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
