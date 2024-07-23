# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 'xtajn'


def func2():
    return (10, 27, 12)


x = lambda x: x()

a = x(func1)

b = x(func2)
