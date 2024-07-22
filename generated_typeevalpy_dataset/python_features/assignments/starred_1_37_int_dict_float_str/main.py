# Functions are assigned to variables via starred assignment
def func1():
    return 30


def func2():
    return {'tjtaq': 56, 'tqpdq': 12, 'tbsne': 17}


def func3():
    return 45.25


def func4():
    return 'rueup'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
