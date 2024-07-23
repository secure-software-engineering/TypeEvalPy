# Two variables are assigned a value via a tuple assignment.
def func1():
    return 45.35


def func2():
    return {'lmwjd': 12, 'hscfu': 99, 'dyrgx': 26}


def func3():
    return 'gndxy'


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
