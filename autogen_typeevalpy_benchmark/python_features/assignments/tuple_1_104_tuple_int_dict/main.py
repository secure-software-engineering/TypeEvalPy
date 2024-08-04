# Two variables are assigned a value via a tuple assignment.
def func1():
    return (31, 29, 41)


def func2():
    return 71


def func3():
    return {'ioqzx': 92, 'vsnyx': 7, 'kzemp': 100}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
