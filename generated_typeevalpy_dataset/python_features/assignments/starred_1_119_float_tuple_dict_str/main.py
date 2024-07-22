# Functions are assigned to variables via starred assignment
def func1():
    return 29.84


def func2():
    return (59, 82, 25)


def func3():
    return {'rtgge': 6, 'qchce': 63, 'xaown': 9}


def func4():
    return 'dfqcf'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
