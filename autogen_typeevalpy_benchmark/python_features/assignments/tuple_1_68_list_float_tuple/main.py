# Two variables are assigned a value via a tuple assignment.
def func1():
    return [36, 83, 55]


def func2():
    return 27.38


def func3():
    return (51, 56, 96)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
