# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 97.4

    def func2(self):
        return (45, 11, 25)

    def func3(self):
        return {'wkkeu': 58, 'nioou': 73, 'vewni': 72}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
