# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return {'lebim': 98, 'nvheb': 44, 'raglr': 35}


def func2():
    return False


x = lambda x: x()

a = x(func1)

b = x(func2)
