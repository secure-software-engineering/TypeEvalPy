# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 51.69

    def func2(self):
        return {'tiqoc': 59, 'eeomi': 2, 'khtgj': 91}

    def func3(self):
        return 'gulkp'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
