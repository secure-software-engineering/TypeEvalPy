# Two variables are assigned a value via a tuple assignment.
def func1():
    return 82.33


def func2():
    return 38


def func3():
    return 'bbjyy'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
