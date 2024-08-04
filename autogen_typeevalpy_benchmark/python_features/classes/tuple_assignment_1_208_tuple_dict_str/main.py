# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (16, 30, 57)

    def func2(self):
        return {'rrzwk': 1, 'gqzbd': 57, 'bsrdd': 49}

    def func3(self):
        return 'rcqbn'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
