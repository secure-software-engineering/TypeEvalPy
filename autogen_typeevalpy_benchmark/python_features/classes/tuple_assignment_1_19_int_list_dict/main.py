# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 95

    def func2(self):
        return [39, 57, 2]

    def func3(self):
        return {'osxbk': 6, 'mcvka': 9, 'fbfhi': 51}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
