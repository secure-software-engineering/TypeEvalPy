# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return {'urgai': 100, 'cdqzl': 91, 'speqb': 36}


def func2():
    return [49, 50, 57]


x = lambda x: x()

a = x(func1)

b = x(func2)
