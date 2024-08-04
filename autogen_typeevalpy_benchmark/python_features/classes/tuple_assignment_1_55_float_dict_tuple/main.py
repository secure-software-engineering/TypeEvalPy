# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 2.55

    def func2(self):
        return {'qrtld': 92, 'lipvy': 76, 'ylhqo': 71}

    def func3(self):
        return (59, 86, 5)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
