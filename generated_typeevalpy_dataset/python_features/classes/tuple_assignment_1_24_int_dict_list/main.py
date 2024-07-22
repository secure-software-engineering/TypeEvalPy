# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 97

    def func2(self):
        return {'jdjvc': 51, 'wloxc': 17, 'aduvw': 100}

    def func3(self):
        return [11, 34, 33]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
