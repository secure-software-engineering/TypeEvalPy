# Functions are assigned to variables via starred assignment
def func1():
    return 27


def func2():
    return 21.25


def func3():
    return {'tkloa': 82, 'uezok': 87, 'sqsjw': 33}


def func4():
    return 'phlxd'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
