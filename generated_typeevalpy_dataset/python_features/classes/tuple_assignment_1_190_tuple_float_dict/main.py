# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (57, 58, 18)

    def func2(self):
        return 23.18

    def func3(self):
        return {'eetxv': 100, 'vsknd': 16, 'npqjz': 77}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
