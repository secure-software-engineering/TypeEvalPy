# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'vxlpt': 83, 'whbtb': 57, 'qqckr': 49}

    def func2(self):
        return [21, 72, 68]

    def func3(self):
        return 61


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
