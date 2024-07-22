# Two variables are assigned a value via a tuple assignment.
def func1():
    return (90, 61, 29)


def func2():
    return [95, 86, 68]


def func3():
    return {'nomvo': 39, 'nmhii': 72, 'mtyfz': 37}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
