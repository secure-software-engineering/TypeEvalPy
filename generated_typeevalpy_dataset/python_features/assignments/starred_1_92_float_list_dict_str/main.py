# Functions are assigned to variables via starred assignment
def func1():
    return 29.35


def func2():
    return [99, 8, 52]


def func3():
    return {'hjhwh': 91, 'nxucy': 91, 'ouqjq': 25}


def func4():
    return 'jithh'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
