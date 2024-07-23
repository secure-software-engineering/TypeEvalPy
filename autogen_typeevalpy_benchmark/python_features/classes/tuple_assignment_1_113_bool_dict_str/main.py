# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return False

    def func2(self):
        return {'ouopl': 9, 'lfefo': 73, 'havij': 36}

    def func3(self):
        return 'rdcwx'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
