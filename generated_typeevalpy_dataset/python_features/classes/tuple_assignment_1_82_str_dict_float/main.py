# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 'bzmzm'

    def func2(self):
        return {'fzoou': 86, 'wzxsy': 51, 'tkbsc': 46}

    def func3(self):
        return 14.45


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
