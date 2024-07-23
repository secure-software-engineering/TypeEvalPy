# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 68.31

    def func2(self):
        return (24, 59, 52)

    def func3(self):
        return {'ghfdk': 52, 'vfagi': 98, 'eycbx': 78}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
