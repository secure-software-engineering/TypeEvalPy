# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 'bvqmb'

    def func2(self):
        return [56, 25, 19]

    def func3(self):
        return {'uuppf': 65, 'nexsw': 72, 'icehg': 6}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
