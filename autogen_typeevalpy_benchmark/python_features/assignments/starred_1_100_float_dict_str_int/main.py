# Functions are assigned to variables via starred assignment
def func1():
    return 14.44


def func2():
    return {'sxxul': 88, 'mspxu': 31, 'dyviz': 69}


def func3():
    return 'ismtt'


def func4():
    return 39

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
