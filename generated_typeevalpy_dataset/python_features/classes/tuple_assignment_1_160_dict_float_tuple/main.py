# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'uyrvp': 19, 'bisxl': 83, 'mivda': 36}

    def func2(self):
        return 45.24

    def func3(self):
        return (85, 49, 1)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
