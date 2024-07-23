# Two variables are assigned a value via a tuple assignment.
def func1():
    return 36


def func2():
    return 90.13


def func3():
    return {'kjpkh': 91, 'nafwz': 5, 'kjfjz': 12}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
