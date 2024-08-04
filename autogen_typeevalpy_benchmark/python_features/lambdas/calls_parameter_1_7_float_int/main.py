# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 59.38


def func2():
    return 7


x = lambda x: x()

a = x(func1)

b = x(func2)
