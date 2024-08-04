# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'mzlhi': 90, 'wyfau': 52, 'jkxbx': 28}

    def func2(self):
        return 76.79

    def func3(self):
        return 'gcubl'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
