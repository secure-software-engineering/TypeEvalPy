# Two variables are assigned a value via a tuple assignment.
def func1():
    return 44


def func2():
    return (29, 98, 63)


def func3():
    return [79, 64, 87]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
