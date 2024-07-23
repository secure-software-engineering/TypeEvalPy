# Two variables are assigned a value via a tuple assignment.
def func1():
    return 50


def func2():
    return [88, 39, 3]


def func3():
    return {'xtpuh': 14, 'fpxzh': 65, 'tfpdz': 60}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
