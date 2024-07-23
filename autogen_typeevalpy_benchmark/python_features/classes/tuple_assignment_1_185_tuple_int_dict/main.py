# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (94, 33, 2)

    def func2(self):
        return 83

    def func3(self):
        return {'awyhp': 64, 'xnuca': 48, 'uunsq': 39}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
