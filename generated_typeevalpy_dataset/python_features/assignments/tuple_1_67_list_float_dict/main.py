# Two variables are assigned a value via a tuple assignment.
def func1():
    return [63, 68, 72]


def func2():
    return 85.81


def func3():
    return {'jzxrr': 48, 'embih': 90, 'bmnir': 60}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
