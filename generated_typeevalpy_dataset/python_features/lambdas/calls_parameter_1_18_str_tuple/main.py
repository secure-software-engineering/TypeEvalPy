# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 'cvcxq'


def func2():
    return (86, 52, 48)


x = lambda x: x()

a = x(func1)

b = x(func2)