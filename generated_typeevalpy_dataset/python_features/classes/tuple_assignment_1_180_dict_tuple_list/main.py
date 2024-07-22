# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'ifuxq': 10, 'saxml': 89, 'omamb': 35}

    def func2(self):
        return (62, 23, 95)

    def func3(self):
        return [19, 8, 94]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
