# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return False


def func2():
    return {'twzdq': 4, 'kuqkx': 4, 'dalsa': 11}


x = lambda x: x()

a = x(func1)

b = x(func2)
