# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'dtdzk': 30, 'svpus': 1, 'txnbn': 34}

    def func2(self):
        return 10

    def func3(self):
        return 39.78


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
