# Two variables are assigned a value via a tuple assignment.
def func1():
    return 90


def func2():
    return 11.04


def func3():
    return (55, 11, 20)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
