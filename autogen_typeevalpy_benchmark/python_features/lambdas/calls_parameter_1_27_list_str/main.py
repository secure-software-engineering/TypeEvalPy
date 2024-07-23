# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return [78, 49, 10]


def func2():
    return 'exwdr'


x = lambda x: x()

a = x(func1)

b = x(func2)
