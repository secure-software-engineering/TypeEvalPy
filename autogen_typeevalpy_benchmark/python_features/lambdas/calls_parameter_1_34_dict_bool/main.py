# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return {'fojid': 3, 'zyslu': 87, 'qaefl': 75}


def func2():
    return True


x = lambda x: x()

a = x(func1)

b = x(func2)
