# Functions are assigned to variables via starred assignment
def func1():
    return 27.79


def func2():
    return {'mxpxe': 48, 'idhdl': 30, 'idssy': 39}


def func3():
    return 'hmcyr'


def func4():
    return (11, 40, 13)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
