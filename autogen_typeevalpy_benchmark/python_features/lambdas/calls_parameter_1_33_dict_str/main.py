# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return {'cenex': 25, 'skiuk': 12, 'rfsvo': 5}


def func2():
    return 'wwlog'


x = lambda x: x()

a = x(func1)

b = x(func2)
