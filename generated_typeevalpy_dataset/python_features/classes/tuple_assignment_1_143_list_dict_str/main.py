# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [28, 28, 75]

    def func2(self):
        return {'tvwqi': 46, 'esnxm': 2, 'zmkjt': 67}

    def func3(self):
        return 'ifltt'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
