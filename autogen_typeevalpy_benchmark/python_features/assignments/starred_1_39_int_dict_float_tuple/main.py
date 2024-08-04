# Functions are assigned to variables via starred assignment
def func1():
    return 11


def func2():
    return {'qvilb': 63, 'quapg': 45, 'pqnlv': 82}


def func3():
    return 46.84


def func4():
    return (7, 81, 30)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
