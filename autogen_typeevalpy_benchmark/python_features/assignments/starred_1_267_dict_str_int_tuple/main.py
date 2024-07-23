# Functions are assigned to variables via starred assignment
def func1():
    return {'pyuyo': 57, 'fmztj': 59, 'qrqyj': 84}


def func2():
    return 'leobq'


def func3():
    return 53


def func4():
    return (3, 73, 1)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
