# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [7, 62, 96]

    def func2(self):
        return 74

    def func3(self):
        return {'fxtiy': 83, 'uwfqu': 62, 'dwpdw': 83}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
