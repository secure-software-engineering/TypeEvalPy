# Functions are assigned to variables via starred assignment
def func1():
    return [79, 68, 95]


def func2():
    return 28.02


def func3():
    return 'ueoqv'


def func4():
    return {'zqikk': 95, 'suucj': 39, 'waelx': 60}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
