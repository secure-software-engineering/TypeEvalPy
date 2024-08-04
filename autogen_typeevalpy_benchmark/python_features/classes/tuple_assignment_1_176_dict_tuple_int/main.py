# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'phyew': 40, 'zvakl': 34, 'paqul': 70}

    def func2(self):
        return (23, 83, 99)

    def func3(self):
        return 77


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
