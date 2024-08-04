# Two variables are assigned a value via a tuple assignment.
def func1():
    return [36, 12, 46]


def func2():
    return 1.13


def func3():
    return {'wfvsv': 38, 'ibtdj': 51, 'fnqlf': 60}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
