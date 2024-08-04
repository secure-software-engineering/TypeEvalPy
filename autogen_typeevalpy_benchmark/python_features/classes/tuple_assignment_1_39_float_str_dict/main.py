# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 79.53

    def func2(self):
        return 'ylxnq'

    def func3(self):
        return {'bafho': 17, 'qgzbz': 97, 'chiqg': 54}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
