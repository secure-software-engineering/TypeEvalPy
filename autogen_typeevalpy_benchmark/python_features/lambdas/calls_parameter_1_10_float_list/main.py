# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 22.4


def func2():
    return [78, 88, 12]


x = lambda x: x()

a = x(func1)

b = x(func2)
