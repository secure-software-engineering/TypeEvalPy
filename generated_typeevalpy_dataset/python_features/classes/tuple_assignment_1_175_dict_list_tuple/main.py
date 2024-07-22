# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'ntpyy': 87, 'elwlv': 98, 'cxcrq': 95}

    def func2(self):
        return [54, 26, 32]

    def func3(self):
        return (90, 89, 93)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
