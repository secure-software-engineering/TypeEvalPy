# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'axizx': 74, 'yurey': 42, 'mnsum': 87}

    def func2(self):
        return [65, 72, 64]

    def func3(self):
        return (8, 92, 72)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
