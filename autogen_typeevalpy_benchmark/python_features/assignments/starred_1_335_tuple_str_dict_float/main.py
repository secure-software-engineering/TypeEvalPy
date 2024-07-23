# Functions are assigned to variables via starred assignment
def func1():
    return (64, 85, 79)


def func2():
    return 'kyfeu'


def func3():
    return {'yielj': 84, 'gcaxk': 40, 'ztkvk': 93}


def func4():
    return 55.88

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
