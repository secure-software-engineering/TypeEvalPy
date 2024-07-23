# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return {'aoyrb': 7, 'fhcoh': 36, 'nybrz': 11}


def func2():
    return 'wvfrn'


x = lambda x: x()

a = x(func1)

b = x(func2)
