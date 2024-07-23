# Two variables are assigned a value via a tuple assignment.
def func1():
    return 36.09


def func2():
    return (18, 38, 29)


def func3():
    return [24, 31, 79]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
