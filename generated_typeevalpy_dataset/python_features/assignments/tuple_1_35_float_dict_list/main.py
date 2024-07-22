# Two variables are assigned a value via a tuple assignment.
def func1():
    return 95.09


def func2():
    return {'sqhrr': 58, 'ljttl': 23, 'vtdzo': 35}


def func3():
    return [72, 77, 2]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
