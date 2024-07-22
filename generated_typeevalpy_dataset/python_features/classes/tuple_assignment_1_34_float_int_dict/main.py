# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 91.76

    def func2(self):
        return 69

    def func3(self):
        return {'vacij': 90, 'kkpgx': 27, 'strrs': 56}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
