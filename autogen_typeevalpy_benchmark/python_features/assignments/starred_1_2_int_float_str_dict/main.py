# Functions are assigned to variables via starred assignment
def func1():
    return 75


def func2():
    return 89.38


def func3():
    return 'elcci'


def func4():
    return {'tpeyc': 20, 'yqkdx': 29, 'qmrvm': 8}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
