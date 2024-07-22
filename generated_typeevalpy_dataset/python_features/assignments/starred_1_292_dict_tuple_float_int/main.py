# Functions are assigned to variables via starred assignment
def func1():
    return {'kpmoa': 8, 'ompir': 49, 'glmtk': 96}


def func2():
    return (82, 13, 68)


def func3():
    return 4.79


def func4():
    return 19

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
