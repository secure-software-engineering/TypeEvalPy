# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'llogq': 71, 'izcja': 23, 'fwftt': 84}

    def func2(self):
        return 94

    def func3(self):
        return [21, 9, 57]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
