# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 29

    def func2(self):
        return (31, 46, 19)

    def func3(self):
        return {'olpcs': 36, 'fupkm': 87, 'enitg': 47}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
