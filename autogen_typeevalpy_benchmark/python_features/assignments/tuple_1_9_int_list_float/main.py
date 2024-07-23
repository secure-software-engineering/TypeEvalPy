# Two variables are assigned a value via a tuple assignment.
def func1():
    return 9


def func2():
    return [17, 49, 64]


def func3():
    return 74.09


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
