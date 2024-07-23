# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return {'cyljm': 8, 'iztar': 64, 'nifnp': 94}


def func2():
    return False


x = lambda x: x()

a = x(func1)

b = x(func2)
