# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'nhzgw': 25, 'kabqg': 19, 'qfqcf': 5}

    def func2(self):
        return (12, 10, 67)

    def func3(self):
        return 25


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
