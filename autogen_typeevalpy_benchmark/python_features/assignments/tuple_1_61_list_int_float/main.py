# Two variables are assigned a value via a tuple assignment.
def func1():
    return [25, 31, 34]


def func2():
    return 30


def func3():
    return 96.48


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
