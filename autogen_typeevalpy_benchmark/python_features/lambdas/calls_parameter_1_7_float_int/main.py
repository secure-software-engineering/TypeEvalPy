# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 20.96


def func2():
    return 28


x = lambda x: x()

a = x(func1)

b = x(func2)
