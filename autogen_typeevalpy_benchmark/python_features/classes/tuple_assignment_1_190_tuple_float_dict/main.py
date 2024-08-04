# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (35, 77, 11)

    def func2(self):
        return 80.33

    def func3(self):
        return {'wzlnm': 80, 'mnxch': 49, 'lswej': 41}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
