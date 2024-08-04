# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (2, 1, 54)

    def func2(self):
        return True

    def func3(self):
        return {'fjhsl': 11, 'keqwz': 9, 'hisvv': 72}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
