# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [52, 8, 29]

    def func2(self):
        return 'nypjq'

    def func3(self):
        return {'idhrk': 41, 'dvmli': 2, 'tgyth': 56}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
