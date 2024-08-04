# Two variables are assigned a value via a tuple assignment.
def func1():
    return 94.09


def func2():
    return [88, 96, 67]


def func3():
    return 'ccabr'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
