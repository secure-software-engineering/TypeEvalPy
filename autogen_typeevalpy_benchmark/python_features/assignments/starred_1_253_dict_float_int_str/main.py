# Functions are assigned to variables via starred assignment
def func1():
    return {'gvnpk': 36, 'oizwi': 55, 'fnrwz': 41}


def func2():
    return 16.56


def func3():
    return 85


def func4():
    return 'nofqa'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
