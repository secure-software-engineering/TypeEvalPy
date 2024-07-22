# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 53

    def func2(self):
        return (26, 58, 19)

    def func3(self):
        return {'zfdwz': 40, 'nwtud': 24, 'hbxex': 47}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
