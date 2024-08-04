# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return False


def func2():
    return {'ehtfu': 26, 'huiuh': 72, 'nsgln': 89}


x = lambda x: x()

a = x(func1)

b = x(func2)
