# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'mmdpl': 40, 'auryc': 20, 'szguj': 67}

    def func2(self):
        return (8, 39, 9)

    def func3(self):
        return 'ksbgo'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
