# Two variables are assigned a value via a tuple assignment.
def func1():
    return [35, 59, 31]


def func2():
    return 39


def func3():
    return 63.31


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
