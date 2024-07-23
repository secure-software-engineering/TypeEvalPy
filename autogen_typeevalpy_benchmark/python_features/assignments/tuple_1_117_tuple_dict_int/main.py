# Two variables are assigned a value via a tuple assignment.
def func1():
    return (31, 50, 96)


def func2():
    return {'zusgc': 49, 'ynbaf': 85, 'irgbw': 73}


def func3():
    return 21


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
