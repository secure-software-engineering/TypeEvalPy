# Two variables are assigned a value via a tuple assignment.
def func1():
    return (56, 57, 33)


def func2():
    return 59


def func3():
    return 71.82


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
