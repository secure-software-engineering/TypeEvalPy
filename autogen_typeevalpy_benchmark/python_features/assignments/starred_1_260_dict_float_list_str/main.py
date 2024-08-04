# Functions are assigned to variables via starred assignment
def func1():
    return {'aagpq': 40, 'zwyqh': 36, 'hmxrw': 15}


def func2():
    return 85.15


def func3():
    return [6, 58, 52]


def func4():
    return 'pvtdq'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
