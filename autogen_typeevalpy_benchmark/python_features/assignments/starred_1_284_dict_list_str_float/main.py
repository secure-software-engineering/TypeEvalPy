# Functions are assigned to variables via starred assignment
def func1():
    return {'pqpnx': 86, 'sbuyk': 58, 'gfsxm': 62}


def func2():
    return [61, 4, 90]


def func3():
    return 'ajygn'


def func4():
    return 89.51

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
