# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [96, 49, 7]

    def func2(self):
        return True

    def func3(self):
        return {'otfac': 84, 'rqzqm': 78, 'vggfz': 61}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
