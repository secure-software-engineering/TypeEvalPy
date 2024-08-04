# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [67, 45, 97]

    def func2(self):
        return {'xdeld': 33, 'zcheq': 24, 'mdims': 13}

    def func3(self):
        return (87, 40, 93)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
