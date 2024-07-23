# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [91, 39, 97]

    def func2(self):
        return (100, 97, 47)

    def func3(self):
        return {'onpam': 40, 'upeyp': 6, 'krupw': 1}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
