# Two variables are assigned a value via a tuple assignment.
def func1():
    return 97


def func2():
    return (11, 35, 67)


def func3():
    return [86, 47, 57]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
