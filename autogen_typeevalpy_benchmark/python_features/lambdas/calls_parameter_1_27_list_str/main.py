# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return [97, 44, 23]


def func2():
    return 'zjmrh'


x = lambda x: x()

a = x(func1)

b = x(func2)
