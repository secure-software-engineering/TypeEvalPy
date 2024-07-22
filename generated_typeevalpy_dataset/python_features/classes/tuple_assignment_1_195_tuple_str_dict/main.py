# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (44, 56, 92)

    def func2(self):
        return 'xxzim'

    def func3(self):
        return {'pyaay': 83, 'hdwpr': 80, 'svyrm': 12}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
