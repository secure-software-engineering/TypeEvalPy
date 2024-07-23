# Two variables are assigned a value via a tuple assignment.
def func1():
    return 78.82


def func2():
    return 55


def func3():
    return (52, 53, 8)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
