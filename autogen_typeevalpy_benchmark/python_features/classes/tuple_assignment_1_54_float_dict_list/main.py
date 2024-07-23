# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 43.47

    def func2(self):
        return {'zojjk': 52, 'qxgui': 45, 'crapy': 42}

    def func3(self):
        return [19, 51, 46]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
