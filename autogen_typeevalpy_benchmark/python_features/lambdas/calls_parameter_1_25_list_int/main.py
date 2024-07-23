# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return [38, 99, 90]


def func2():
    return 85


x = lambda x: x()

a = x(func1)

b = x(func2)
