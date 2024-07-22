# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 'oruxb'

    def func2(self):
        return 11.12

    def func3(self):
        return {'ippua': 1, 'ytdmh': 96, 'wervz': 64}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
