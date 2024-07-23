# Functions are assigned to variables via starred assignment
def func1():
    return [67, 26, 8]


def func2():
    return 40.99


def func3():
    return 'jyjur'


def func4():
    return {'nxmoq': 40, 'isxcj': 77, 'hgcnl': 82}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
