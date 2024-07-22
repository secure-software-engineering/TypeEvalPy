# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'uveyo': 35, 'aoblt': 32, 'nrjet': 72}

    def func2(self):
        return 'trbdf'

    def func3(self):
        return (74, 9, 84)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
