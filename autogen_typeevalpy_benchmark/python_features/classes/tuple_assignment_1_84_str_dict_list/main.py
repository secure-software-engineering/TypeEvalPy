# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 'eejko'

    def func2(self):
        return {'dysvf': 99, 'gdriv': 19, 'ojywq': 62}

    def func3(self):
        return [44, 1, 48]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
