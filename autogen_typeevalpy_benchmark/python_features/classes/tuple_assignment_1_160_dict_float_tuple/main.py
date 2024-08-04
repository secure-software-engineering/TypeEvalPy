# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return {'juity': 58, 'vopix': 21, 'jxlqd': 96}

    def func2(self):
        return 73.1

    def func3(self):
        return (80, 45, 62)


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
