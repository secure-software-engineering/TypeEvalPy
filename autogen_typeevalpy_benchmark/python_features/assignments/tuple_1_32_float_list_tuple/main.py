# Two variables are assigned a value via a tuple assignment.
def func1():
    return 15.23


def func2():
    return [96, 97, 64]


def func3():
    return (81, 20, 41)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
