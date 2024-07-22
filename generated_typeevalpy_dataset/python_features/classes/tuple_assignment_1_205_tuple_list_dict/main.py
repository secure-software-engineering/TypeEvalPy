# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (65, 79, 10)

    def func2(self):
        return [13, 57, 31]

    def func3(self):
        return {'kxnhm': 36, 'xrwuc': 47, 'cziae': 83}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
