# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return [29, 19, 92]

    def func2(self):
        return 'lgqkh'

    def func3(self):
        return {'cgcaj': 48, 'zldcs': 85, 'wjkej': 67}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
