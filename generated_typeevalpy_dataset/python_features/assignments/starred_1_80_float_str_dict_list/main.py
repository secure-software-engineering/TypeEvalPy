# Functions are assigned to variables via starred assignment
def func1():
    return 57.71


def func2():
    return 'rkqnv'


def func3():
    return {'kwzgk': 80, 'ibfld': 48, 'leffc': 93}


def func4():
    return [91, 57, 56]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
