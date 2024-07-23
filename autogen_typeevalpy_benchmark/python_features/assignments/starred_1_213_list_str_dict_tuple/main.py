# Functions are assigned to variables via starred assignment
def func1():
    return [68, 40, 9]


def func2():
    return 'zovon'


def func3():
    return {'vcial': 23, 'gfowo': 86, 'upwja': 93}


def func4():
    return (96, 88, 63)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
