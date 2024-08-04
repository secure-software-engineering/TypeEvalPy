# Two variables are assigned a value via a tuple assignment.
def func1():
    return {'ccvee': 1, 'hasrt': 86, 'sylmb': 86}


def func2():
    return [31, 70, 72]


def func3():
    return 82


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
