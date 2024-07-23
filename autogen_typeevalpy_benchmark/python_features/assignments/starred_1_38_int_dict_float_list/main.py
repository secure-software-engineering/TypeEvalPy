# Functions are assigned to variables via starred assignment
def func1():
    return 89


def func2():
    return {'erhfg': 98, 'lueqk': 40, 'taumf': 60}


def func3():
    return 66.7


def func4():
    return [90, 99, 90]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
