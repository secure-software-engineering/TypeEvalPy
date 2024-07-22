# Two variables are assigned a value via a tuple assignment.
def func1():
    return 79.17


def func2():
    return 2


def func3():
    return (2, 66, 18)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
