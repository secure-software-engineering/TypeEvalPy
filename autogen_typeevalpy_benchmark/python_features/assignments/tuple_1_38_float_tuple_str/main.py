# Two variables are assigned a value via a tuple assignment.
def func1():
    return 74.88


def func2():
    return (82, 39, 29)


def func3():
    return 'hpmto'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
