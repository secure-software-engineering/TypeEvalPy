# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'mmvca': 37, 'uvmyd': 33, 'jyacj': 80}

    def func2(self):
        return [37, 5, 82]

    def func3(self):
        return 'vqqnl'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
