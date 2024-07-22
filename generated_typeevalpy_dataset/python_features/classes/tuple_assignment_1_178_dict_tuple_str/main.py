# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'gbjpv': 95, 'fgbit': 80, 'ecmxe': 57}

    def func2(self):
        return (19, 100, 59)

    def func3(self):
        return 'dtxvi'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
