# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (89, 83, 49)

    def func2(self):
        return {'hznbx': 53, 'nrzrw': 94, 'vbrrh': 16}

    def func3(self):
        return 73


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
