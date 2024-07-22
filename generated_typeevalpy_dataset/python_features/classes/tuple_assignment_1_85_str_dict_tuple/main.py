# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 'rnhpl'

    def func2(self):
        return {'ukygf': 26, 'zzymb': 9, 'viamh': 12}

    def func3(self):
        return (88, 27, 3)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
