# Functions are assigned to variables via starred assignment
def func1():
    return {'zgmbl': 6, 'pxpsi': 53, 'ilzxd': 15}


def func2():
    return 'mbkiy'


def func3():
    return 47


def func4():
    return 56.8

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
