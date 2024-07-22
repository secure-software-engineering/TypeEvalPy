# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 9.74

    def func2(self):
        return (98, 29, 51)

    def func3(self):
        return {'xloix': 93, 'owkli': 38, 'zkcjo': 74}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
