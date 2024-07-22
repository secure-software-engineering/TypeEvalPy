# Two variables are assigned a value via a tuple assignment.
def func1():
    return [39, 25, 96]


def func2():
    return 41


def func3():
    return 'ldsdq'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
