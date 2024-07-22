# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'nrkqh': 35, 'isqxt': 35, 'cnmyc': 91}

    def func2(self):
        return 85

    def func3(self):
        return (67, 24, 16)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
