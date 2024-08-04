# Functions are assigned to variables via starred assignment
def func1():
    return 'dywpi'


def func2():
    return 8


def func3():
    return 42.28


def func4():
    return {'ryxua': 94, 'zxtzj': 68, 'qaxxw': 82}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
