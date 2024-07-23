# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'pusiy': 73, 'oucik': 2, 'vrjhh': 83}

    def func2(self):
        return 3

    def func3(self):
        return 'oanii'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
