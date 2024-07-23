# Two variables are assigned a value via a tuple assignment.
def func1():
    return (18, 24, 82)


def func2():
    return 21


def func3():
    return 68.38


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
