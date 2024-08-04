# Two variables are assigned a value via a tuple assignment.
def func1():
    return 96.11


def func2():
    return 'qhdds'


def func3():
    return [92, 16, 1]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
