# Functions are assigned to variables via starred assignment
def func1():
    return [64, 51, 80]


def func2():
    return 70.05


def func3():
    return {'uiyhs': 67, 'hhuhm': 26, 'hfdxx': 13}


def func4():
    return 'ysnpo'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
