# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 44.93

    def func2(self):
        return {'dkyxs': 67, 'ztral': 21, 'geykd': 45}

    def func3(self):
        return [38, 50, 31]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
