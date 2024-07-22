# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 25


def func2():
    return [60, 92, 76]


x = lambda x: x()

a = x(func1)

b = x(func2)
