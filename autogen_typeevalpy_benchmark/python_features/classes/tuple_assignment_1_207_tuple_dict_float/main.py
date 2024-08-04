# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (71, 49, 42)

    def func2(self):
        return {'xgtch': 45, 'ztqyt': 6, 'tmqnb': 9}

    def func3(self):
        return 33.51


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
