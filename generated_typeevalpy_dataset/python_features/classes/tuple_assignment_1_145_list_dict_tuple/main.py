# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [68, 93, 9]

    def func2(self):
        return {'nezob': 73, 'dlhsu': 4, 'zmgen': 34}

    def func3(self):
        return (31, 30, 4)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
