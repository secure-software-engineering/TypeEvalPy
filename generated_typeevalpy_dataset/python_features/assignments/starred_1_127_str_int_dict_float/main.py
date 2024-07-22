# Functions are assigned to variables via starred assignment
def func1():
    return 'frhuz'


def func2():
    return 15


def func3():
    return {'wbuyk': 76, 'vptlj': 7, 'gjrbg': 19}


def func4():
    return 72.73

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
