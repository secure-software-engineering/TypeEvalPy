# Functions are assigned to variables via starred assignment
def func1():
    return 'atzkp'


def func2():
    return 78.31


def func3():
    return 76


def func4():
    return [13, 74, 1]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
