# Two variables are assigned a value via a tuple assignment.
def func1():
    return {'govlo': 85, 'pziye': 19, 'lqphn': 48}


def func2():
    return [57, 18, 38]


def func3():
    return 56.56


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
