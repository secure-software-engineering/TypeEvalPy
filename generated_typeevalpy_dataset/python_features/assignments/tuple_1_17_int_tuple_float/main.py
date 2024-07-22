# Two variables are assigned a value via a tuple assignment.
def func1():
    return 81


def func2():
    return (47, 42, 20)


def func3():
    return 16.77


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
