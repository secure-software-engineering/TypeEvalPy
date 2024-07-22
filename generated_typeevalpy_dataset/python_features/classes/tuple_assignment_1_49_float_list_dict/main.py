# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 29.44

    def func2(self):
        return [68, 4, 5]

    def func3(self):
        return {'izclu': 67, 'loimv': 43, 'zlxwl': 49}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
