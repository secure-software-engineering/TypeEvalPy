# Two variables are assigned a value via a tuple assignment.
def func1():
    return [68, 52, 61]


def func2():
    return 'ueiyy'


def func3():
    return 36.23


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
