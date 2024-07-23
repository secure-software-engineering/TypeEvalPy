# Functions are assigned to variables via starred assignment
def func1():
    return 35


def func2():
    return [72, 20, 9]


def func3():
    return 51.58


def func4():
    return {'osmjb': 80, 'iheoi': 33, 'evctt': 9}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
