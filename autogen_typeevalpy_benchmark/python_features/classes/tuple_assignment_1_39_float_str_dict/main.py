# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 12.51

    def func2(self):
        return 'xiavh'

    def func3(self):
        return {'wvazh': 41, 'bksda': 80, 'vranb': 10}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
