# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (5, 45, 86)

    def func2(self):
        return 'vlgdk'

    def func3(self):
        return {'vhyvj': 60, 'qwlkb': 74, 'atfuj': 13}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
