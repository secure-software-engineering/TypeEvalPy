# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'kpveh': 66, 'tfjag': 67, 'cygvc': 39}

    def func2(self):
        return [37, 93, 73]

    def func3(self):
        return 40.13


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
