# Functions are assigned to variables via starred assignment
def func1():
    return [52, 24, 72]


def func2():
    return {'ikmxh': 55, 'vhlku': 58, 'lorip': 35}


def func3():
    return 57.64


def func4():
    return 'zqqdi'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
