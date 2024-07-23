# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return (67, 67, 9)


def func2():
    return {'hmkox': 16, 'rysxg': 33, 'omeqt': 75}


x = lambda x: x()

a = x(func1)

b = x(func2)
