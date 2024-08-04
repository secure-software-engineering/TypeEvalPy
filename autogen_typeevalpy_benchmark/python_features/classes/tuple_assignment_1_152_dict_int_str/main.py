# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'cfvdf': 93, 'eamgt': 74, 'xwmyt': 39}

    def func2(self):
        return 27

    def func3(self):
        return 'pvgan'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
