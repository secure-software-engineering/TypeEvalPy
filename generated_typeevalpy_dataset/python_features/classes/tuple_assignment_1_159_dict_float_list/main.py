# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'mdvin': 29, 'lzfaz': 5, 'leqrs': 80}

    def func2(self):
        return 55.3

    def func3(self):
        return [74, 79, 60]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
