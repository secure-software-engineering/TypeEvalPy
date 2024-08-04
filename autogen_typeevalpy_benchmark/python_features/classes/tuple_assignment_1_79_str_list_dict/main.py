# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 'projc'

    def func2(self):
        return [33, 42, 34]

    def func3(self):
        return {'ykdlc': 75, 'wfclp': 46, 'lewuy': 64}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
