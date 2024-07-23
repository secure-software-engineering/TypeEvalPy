# Functions are assigned to variables via starred assignment
def func1():
    return 98


def func2():
    return 62.22


def func3():
    return [27, 74, 16]


def func4():
    return {'jdqzk': 57, 'peeis': 2, 'bxtlm': 81}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
