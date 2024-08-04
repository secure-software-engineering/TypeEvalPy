# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [46, 89, 95]

    def func2(self):
        return (88, 71, 63)

    def func3(self):
        return {'musfh': 17, 'umljd': 75, 'nqkrx': 20}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
