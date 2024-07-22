# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return {'jfgbv': 68, 'ghcxg': 92, 'dotra': 59}


def func2():
    return 72


x = lambda x: x()

a = x(func1)

b = x(func2)
