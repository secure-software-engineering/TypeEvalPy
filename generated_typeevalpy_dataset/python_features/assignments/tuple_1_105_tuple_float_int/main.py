# Two variables are assigned a value via a tuple assignment.
def func1():
    return (2, 91, 90)


def func2():
    return 19.36


def func3():
    return 33


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
