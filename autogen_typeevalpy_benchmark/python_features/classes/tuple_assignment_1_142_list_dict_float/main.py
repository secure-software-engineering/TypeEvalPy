# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [74, 90, 58]

    def func2(self):
        return {'gaqea': 51, 'srjpm': 65, 'onnld': 7}

    def func3(self):
        return 40.28


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
