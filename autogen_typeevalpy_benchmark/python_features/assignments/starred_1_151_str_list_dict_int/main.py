# Functions are assigned to variables via starred assignment
def func1():
    return 'gilrv'


def func2():
    return [100, 18, 28]


def func3():
    return {'djvak': 38, 'msjcq': 87, 'hdnue': 97}


def func4():
    return 66

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
