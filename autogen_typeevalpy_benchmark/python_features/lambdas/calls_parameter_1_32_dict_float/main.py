# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return {'qezsu': 77, 'bgheg': 15, 'yuttt': 61}


def func2():
    return 47.56


x = lambda x: x()

a = x(func1)

b = x(func2)
