# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 51

    def func2(self):
        return False

    def func3(self):
        return {'pmrmu': 95, 'xtlte': 7, 'tjlrg': 28}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
