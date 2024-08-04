# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return 66.2


def func2():
    return {'vphkq': 32, 'vspql': 15, 'mwscr': 50}


x = lambda x: x()

a = x(func1)

b = x(func2)
