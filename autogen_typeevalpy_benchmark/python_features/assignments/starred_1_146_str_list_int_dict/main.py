# Functions are assigned to variables via starred assignment
def func1():
    return 'rguio'


def func2():
    return [35, 57, 57]


def func3():
    return 56


def func4():
    return {'jupaa': 14, 'isguf': 44, 'vftnr': 53}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
