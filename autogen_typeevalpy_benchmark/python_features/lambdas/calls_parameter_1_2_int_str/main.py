# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 87


def func2():
    return 'zshdo'


x = lambda x: x()

a = x(func1)

b = x(func2)
