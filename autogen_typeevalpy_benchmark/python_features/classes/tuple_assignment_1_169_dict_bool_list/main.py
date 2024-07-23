# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'woqdf': 14, 'dssss': 39, 'lmvft': 84}

    def func2(self):
        return False

    def func3(self):
        return [37, 94, 39]


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
