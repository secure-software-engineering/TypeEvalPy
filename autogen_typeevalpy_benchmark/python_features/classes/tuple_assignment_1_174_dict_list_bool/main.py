# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'ijzfg': 53, 'xyojt': 27, 'srkvt': 31}

    def func2(self):
        return [44, 89, 35]

    def func3(self):
        return True


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
