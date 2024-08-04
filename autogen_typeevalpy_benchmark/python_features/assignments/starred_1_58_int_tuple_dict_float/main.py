# Functions are assigned to variables via starred assignment
def func1():
    return 3


def func2():
    return (53, 19, 88)


def func3():
    return {'pyypk': 94, 'uiblw': 65, 'nvdpt': 63}


def func4():
    return 23.63

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
