# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return [11, 14, 76]


def func2():
    return 80.04


x = lambda x: x()

a = x(func1)

b = x(func2)
