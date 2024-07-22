# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'hrwdh': 75, 'epvjb': 96, 'fzszj': 71}

    def func2(self):
        return 26

    def func3(self):
        return [84, 21, 34]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
