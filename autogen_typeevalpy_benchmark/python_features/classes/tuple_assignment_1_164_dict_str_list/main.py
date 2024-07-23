# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'mjyks': 78, 'uekea': 23, 'qvgoi': 99}

    def func2(self):
        return 'aunno'

    def func3(self):
        return [7, 53, 100]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
