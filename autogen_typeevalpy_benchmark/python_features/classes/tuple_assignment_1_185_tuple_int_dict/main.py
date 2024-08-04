# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (93, 62, 31)

    def func2(self):
        return 40

    def func3(self):
        return {'qqita': 6, 'zelur': 43, 'clfbe': 46}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
