# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return (56, 96, 2)


def func2():
    return 33


x = lambda x: x()

a = x(func1)

b = x(func2)
