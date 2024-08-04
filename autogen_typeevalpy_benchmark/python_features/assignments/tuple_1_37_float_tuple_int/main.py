# Two variables are assigned a value via a tuple assignment.
def func1():
    return 47.27


def func2():
    return (12, 4, 97)


def func3():
    return 6


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
