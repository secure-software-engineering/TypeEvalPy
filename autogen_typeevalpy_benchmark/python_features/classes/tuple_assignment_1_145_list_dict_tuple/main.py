# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [30, 70, 45]

    def func2(self):
        return {'jhalc': 48, 'pgilm': 91, 'kjapf': 35}

    def func3(self):
        return (55, 38, 8)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
