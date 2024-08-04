# Two variables are assigned a value via a tuple assignment.
def func1():
    return [68, 6, 90]


def func2():
    return 91.96


def func3():
    return 'vaffz'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
