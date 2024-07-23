# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 'lturx'

    def func2(self):
        return {'dntrn': 11, 'vihdg': 90, 'fhfnc': 29}

    def func3(self):
        return [4, 56, 100]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
