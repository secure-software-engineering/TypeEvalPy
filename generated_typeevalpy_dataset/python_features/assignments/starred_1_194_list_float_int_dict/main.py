# Functions are assigned to variables via starred assignment
def func1():
    return [15, 32, 22]


def func2():
    return 83.17


def func3():
    return 76


def func4():
    return {'wndok': 70, 'huvkc': 48, 'xwhvk': 73}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
