# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return {'nbwxy': 66, 'xvtyh': 86, 'zukyk': 94}


def func2():
    return 86


x = lambda x: x()

a = x(func1)

b = x(func2)
