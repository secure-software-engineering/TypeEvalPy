# Two variables are assigned a value via a tuple assignment.
def func1():
    return [21, 24, 41]


def func2():
    return 34.88


def func3():
    return 'oimic'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
