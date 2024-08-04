# Two variables are assigned a value via a tuple assignment.
def func1():
    return 'defpg'


def func2():
    return 6


def func3():
    return 93.01


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
