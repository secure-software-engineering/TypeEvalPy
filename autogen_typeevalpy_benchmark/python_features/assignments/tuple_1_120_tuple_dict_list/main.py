# Two variables are assigned a value via a tuple assignment.
def func1():
    return (81, 73, 96)


def func2():
    return {'mlvoj': 98, 'cjlap': 90, 'mtzug': 9}


def func3():
    return [8, 88, 45]


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
