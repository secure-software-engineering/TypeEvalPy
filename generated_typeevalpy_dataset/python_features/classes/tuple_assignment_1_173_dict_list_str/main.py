# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'strxt': 69, 'bviun': 11, 'kdthg': 38}

    def func2(self):
        return [28, 66, 44]

    def func3(self):
        return 'tafpb'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
