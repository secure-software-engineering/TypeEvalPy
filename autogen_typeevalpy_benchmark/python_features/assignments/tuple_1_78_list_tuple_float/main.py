# Two variables are assigned a value via a tuple assignment.
def func1():
    return [63, 3, 26]


def func2():
    return (59, 88, 37)


def func3():
    return 39.73


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
