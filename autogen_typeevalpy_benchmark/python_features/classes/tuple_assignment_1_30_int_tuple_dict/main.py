# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 49

    def func2(self):
        return (76, 42, 47)

    def func3(self):
        return {'lzayb': 51, 'erwdj': 45, 'zxmbh': 83}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
