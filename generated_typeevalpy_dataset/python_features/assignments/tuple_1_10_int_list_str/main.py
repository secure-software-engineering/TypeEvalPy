# Two variables are assigned a value via a tuple assignment.
def func1():
    return 5


def func2():
    return [65, 35, 64]


def func3():
    return 'trogf'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
