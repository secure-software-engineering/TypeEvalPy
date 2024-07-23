# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'otkxx': 66, 'zhgpv': 63, 'xatdb': 1}

    def func2(self):
        return 18

    def func3(self):
        return (37, 31, 16)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
