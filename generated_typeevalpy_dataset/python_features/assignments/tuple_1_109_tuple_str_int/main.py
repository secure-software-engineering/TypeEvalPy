# Two variables are assigned a value via a tuple assignment.
def func1():
    return (62, 44, 91)


def func2():
    return 'mzyfs'


def func3():
    return 23


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
