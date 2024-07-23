# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [21, 53, 73]

    def func2(self):
        return {'fqjjf': 52, 'acmxp': 74, 'taodm': 16}

    def func3(self):
        return 'uyedm'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
