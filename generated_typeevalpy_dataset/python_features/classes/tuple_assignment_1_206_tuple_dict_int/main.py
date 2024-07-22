# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return (46, 35, 60)

    def func2(self):
        return {'drkee': 82, 'azpkd': 83, 'xfsqw': 5}

    def func3(self):
        return 18


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
