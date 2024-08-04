# Functions are assigned to variables via starred assignment
def func1():
    return [8, 95, 56]


def func2():
    return 44.84


def func3():
    return {'jwyff': 45, 'yrkai': 23, 'fupez': 66}


def func4():
    return 'msifv'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
