# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'elpvu': 4, 'susrx': 95, 'jgibp': 21}

    def func2(self):
        return 'lbddj'

    def func3(self):
        return 70


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
