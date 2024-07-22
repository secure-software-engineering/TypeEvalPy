# Functions are assigned to variables via starred assignment
def func1():
    return 83


def func2():
    return {'kxupf': 35, 'fkrcd': 48, 'vtdbq': 87}


def func3():
    return [90, 35, 85]


def func4():
    return 95.22

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
