# Two variables are assigned a value via a tuple assignment.
def func1():
    return 58.35


def func2():
    return [59, 76, 36]


def func3():
    return 76


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
