# Functions are assigned to variables via starred assignment
def func1():
    return (22, 94, 27)


def func2():
    return {'hngfz': 96, 'lkupa': 57, 'aolss': 27}


def func3():
    return 97.64


def func4():
    return 'tkhtu'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
