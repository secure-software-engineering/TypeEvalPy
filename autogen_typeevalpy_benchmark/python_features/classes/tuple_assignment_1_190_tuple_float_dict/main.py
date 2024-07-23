# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (95, 42, 14)

    def func2(self):
        return 39.41

    def func3(self):
        return {'wlrdz': 40, 'iikwv': 17, 'glcea': 21}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
