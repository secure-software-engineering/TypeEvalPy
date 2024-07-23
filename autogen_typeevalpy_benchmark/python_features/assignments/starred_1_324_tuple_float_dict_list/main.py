# Functions are assigned to variables via starred assignment
def func1():
    return (4, 77, 93)


def func2():
    return 93.33


def func3():
    return {'hwcch': 48, 'igakr': 11, 'lhymg': 12}


def func4():
    return [43, 64, 9]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
