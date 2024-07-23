# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 27

    def func2(self):
        return {'xexmk': 37, 'klrgx': 91, 'mvupj': 60}

    def func3(self):
        return (66, 54, 64)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
