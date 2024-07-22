# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 59

    def func2(self):
        return 11.87

    def func3(self):
        return {'yywcm': 21, 'wjbmr': 65, 'ydynr': 8}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
