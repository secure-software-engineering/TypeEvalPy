# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return {'dzbsn': 3, 'vwaka': 23, 'ournk': 33}


def func2():
    return 46.35


x = lambda x: x()

a = x(func1)

b = x(func2)
