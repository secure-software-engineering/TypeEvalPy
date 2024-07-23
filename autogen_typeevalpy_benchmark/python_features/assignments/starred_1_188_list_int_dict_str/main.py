# Functions are assigned to variables via starred assignment
def func1():
    return [78, 7, 60]


def func2():
    return 29


def func3():
    return {'bspiq': 1, 'fmknb': 96, 'vghrp': 24}


def func4():
    return 'gdvhc'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
