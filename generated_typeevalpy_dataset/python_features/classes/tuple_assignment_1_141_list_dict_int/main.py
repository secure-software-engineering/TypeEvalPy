# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [85, 95, 17]

    def func2(self):
        return {'rerzl': 66, 'touqt': 98, 'ccoyb': 60}

    def func3(self):
        return 64


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
