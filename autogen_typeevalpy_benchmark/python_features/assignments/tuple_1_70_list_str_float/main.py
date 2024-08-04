# Two variables are assigned a value via a tuple assignment.
def func1():
    return [61, 34, 15]


def func2():
    return 'idbyo'


def func3():
    return 82.0


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
