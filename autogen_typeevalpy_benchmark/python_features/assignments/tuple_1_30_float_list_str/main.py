# Two variables are assigned a value via a tuple assignment.
def func1():
    return 12.76


def func2():
    return [97, 39, 42]


def func3():
    return 'fbwxp'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
