# Two variables are assigned a value via a tuple assignment.
def func1():
    return [7, 55, 40]


def func2():
    return 9


def func3():
    return {'pwkdk': 1, 'jtsuq': 98, 'icgcz': 48}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
