# Functions are assigned to variables via starred assignment
def func1():
    return 'gyjmn'


def func2():
    return 29.57


def func3():
    return (51, 1, 58)


def func4():
    return {'ouami': 36, 'rxsyp': 39, 'bmjdr': 13}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
