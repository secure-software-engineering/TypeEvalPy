# Two variables are assigned a value via a tuple assignment.
def func1():
    return 19.65


def func2():
    return {'gopcc': 24, 'zsesv': 29, 'remlk': 79}


def func3():
    return (22, 63, 63)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
