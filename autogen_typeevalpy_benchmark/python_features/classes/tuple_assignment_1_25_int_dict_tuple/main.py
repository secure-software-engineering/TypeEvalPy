# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 9

    def func2(self):
        return {'gtvhj': 53, 'mstzn': 97, 'eqjsj': 11}

    def func3(self):
        return (61, 56, 86)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
