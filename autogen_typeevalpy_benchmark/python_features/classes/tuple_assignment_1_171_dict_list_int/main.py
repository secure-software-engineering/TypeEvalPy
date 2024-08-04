# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'hllly': 79, 'trcde': 27, 'jjgir': 15}

    def func2(self):
        return [58, 56, 75]

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
