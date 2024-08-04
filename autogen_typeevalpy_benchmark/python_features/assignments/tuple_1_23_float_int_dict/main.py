# Two variables are assigned a value via a tuple assignment.
def func1():
    return 28.08


def func2():
    return 26


def func3():
    return {'iitva': 20, 'ivvik': 2, 'bejwi': 81}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
