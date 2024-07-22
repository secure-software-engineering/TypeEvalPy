# Two variables are assigned a value via a tuple assignment.
def func1():
    return 79.16


def func2():
    return 85


def func3():
    return {'fcvpd': 51, 'layvi': 26, 'jwsug': 79}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
