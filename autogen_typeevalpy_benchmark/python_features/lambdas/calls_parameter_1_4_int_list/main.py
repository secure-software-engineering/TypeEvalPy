# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 3


def func2():
    return [38, 19, 4]


x = lambda x: x()

a = x(func1)

b = x(func2)
