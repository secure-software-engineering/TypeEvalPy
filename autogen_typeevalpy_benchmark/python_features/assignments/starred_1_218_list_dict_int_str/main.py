# Functions are assigned to variables via starred assignment
def func1():
    return [87, 71, 17]


def func2():
    return {'rjfsp': 66, 'porpm': 82, 'jdjak': 22}


def func3():
    return 6


def func4():
    return 'bglth'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
