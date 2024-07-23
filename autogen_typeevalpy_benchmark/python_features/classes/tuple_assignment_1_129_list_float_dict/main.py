# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [16, 66, 21]

    def func2(self):
        return 36.14

    def func3(self):
        return {'lhkfc': 58, 'umprf': 17, 'qgidg': 46}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
