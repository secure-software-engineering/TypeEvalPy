# Two variables are assigned a value via a tuple assignment.
def func1():
    return [56, 43, 85]


def func2():
    return {'hrwwq': 33, 'mnpew': 32, 'ovgrk': 95}


def func3():
    return (11, 55, 64)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
