# Functions are assigned to variables via starred assignment
def func1():
    return [32, 96, 75]


def func2():
    return 'gamfd'


def func3():
    return (73, 31, 68)


def func4():
    return {'vxgkd': 70, 'cbtgr': 59, 'qakvd': 20}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
