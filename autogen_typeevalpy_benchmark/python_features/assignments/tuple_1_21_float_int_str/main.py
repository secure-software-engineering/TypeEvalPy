# Two variables are assigned a value via a tuple assignment.
def func1():
    return 28.76


def func2():
    return 21


def func3():
    return 'gkmym'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
