# Two variables are assigned a value via a tuple assignment.
def func1():
    return 95.28


def func2():
    return 50


def func3():
    return [51, 93, 80]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
