# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 50

    def func2(self):
        return {'glmty': 89, 'sqwvn': 94, 'ctjwt': 61}

    def func3(self):
        return 'tzqpj'


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
