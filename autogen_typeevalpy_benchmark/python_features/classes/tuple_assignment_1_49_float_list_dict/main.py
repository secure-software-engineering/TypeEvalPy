# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 63.22

    def func2(self):
        return [49, 47, 56]

    def func3(self):
        return {'rmdlf': 14, 'wmlve': 69, 'xailb': 77}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
