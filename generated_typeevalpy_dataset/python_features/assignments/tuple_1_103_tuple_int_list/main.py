# Two variables are assigned a value via a tuple assignment.
def func1():
    return (15, 82, 39)


def func2():
    return 63


def func3():
    return [28, 48, 90]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
