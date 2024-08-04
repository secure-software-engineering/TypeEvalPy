# Two variables are assigned a value via a tuple assignment.
def func1():
    return (1, 1, 46)


def func2():
    return [96, 88, 56]


def func3():
    return 55.44


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
