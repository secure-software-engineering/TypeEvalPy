# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 41.47

    def func2(self):
        return {'wtmze': 79, 'gyxut': 61, 'ifwfs': 41}

    def func3(self):
        return 75


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
