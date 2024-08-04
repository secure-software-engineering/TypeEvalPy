# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return True

    def func2(self):
        return {'avvkl': 15, 'vqekf': 31, 'pcuge': 84}

    def func3(self):
        return (4, 20, 91)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
