# Two variables are assigned a value via a tuple assignment.
def func1():
    return 50


def func2():
    return (11, 16, 98)


def func3():
    return [50, 50, 18]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
