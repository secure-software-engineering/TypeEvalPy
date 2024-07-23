# Two variables are assigned a value via a tuple assignment.
def func1():
    return 1


def func2():
    return (73, 88, 74)


def func3():
    return 38.47


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
