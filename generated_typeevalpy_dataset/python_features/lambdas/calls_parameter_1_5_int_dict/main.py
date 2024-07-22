# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 12


def func2():
    return {'akxqq': 54, 'sgzuh': 86, 'dmxxb': 53}


x = lambda x: x()

a = x(func1)

b = x(func2)
