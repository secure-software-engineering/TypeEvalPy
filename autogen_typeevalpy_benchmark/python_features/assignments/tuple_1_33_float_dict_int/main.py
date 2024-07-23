# Two variables are assigned a value via a tuple assignment.
def func1():
    return 67.93


def func2():
    return {'plgiz': 43, 'owlat': 59, 'wbdrb': 99}


def func3():
    return 78


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
