# Two variables are assigned a value via a tuple assignment.
def func1():
    return [99, 83, 88]


def func2():
    return {'eatak': 24, 'nitbc': 31, 'vsrde': 93}


def func3():
    return 52


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
