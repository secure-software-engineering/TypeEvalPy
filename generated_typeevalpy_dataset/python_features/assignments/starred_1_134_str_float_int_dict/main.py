# Functions are assigned to variables via starred assignment
def func1():
    return 'kptsd'


def func2():
    return 23.92


def func3():
    return 11


def func4():
    return {'ffiie': 17, 'kfpdu': 90, 'fxcgm': 35}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
