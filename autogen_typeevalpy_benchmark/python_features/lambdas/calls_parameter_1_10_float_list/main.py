# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 84.5


def func2():
    return [13, 25, 87]


x = lambda x: x()

a = x(func1)

b = x(func2)
