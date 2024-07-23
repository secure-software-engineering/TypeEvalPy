# Functions are assigned to variables via starred assignment
def func1():
    return [4, 13, 54]


def func2():
    return 99


def func3():
    return 1.87


def func4():
    return {'gynld': 7, 'wyezs': 84, 'xtmbr': 98}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
