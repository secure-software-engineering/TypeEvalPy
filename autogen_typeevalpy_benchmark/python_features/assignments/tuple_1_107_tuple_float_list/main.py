# Two variables are assigned a value via a tuple assignment.
def func1():
    return (5, 47, 20)


def func2():
    return 13.56


def func3():
    return [11, 68, 35]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
