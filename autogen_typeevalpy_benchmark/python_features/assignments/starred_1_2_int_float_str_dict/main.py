# Functions are assigned to variables via starred assignment
def func1():
    return 48


def func2():
    return 90.2


def func3():
    return 'euhmo'


def func4():
    return {'wyssa': 27, 'xzsmw': 30, 'jwhrl': 84}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
