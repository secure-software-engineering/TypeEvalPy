# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (47, 28, 40)

    def func2(self):
        return {'jadta': 27, 'dhmzq': 32, 'eiero': 33}

    def func3(self):
        return [32, 14, 87]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
