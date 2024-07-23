# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return (98, 39, 81)


def func2():
    return 38.45


x = lambda x: x()

a = x(func1)

b = x(func2)
