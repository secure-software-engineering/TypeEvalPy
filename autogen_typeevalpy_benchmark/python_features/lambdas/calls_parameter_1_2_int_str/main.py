# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 66


def func2():
    return 'cngbe'


x = lambda x: x()

a = x(func1)

b = x(func2)
