# Two variables are assigned a value via a tuple assignment.
def func1():
    return (96, 8, 19)


def func2():
    return [59, 93, 41]


def func3():
    return 15


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
