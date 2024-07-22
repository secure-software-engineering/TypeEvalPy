# Functions are assigned to variables via starred assignment
def func1():
    return 31.97


def func2():
    return {'ovwdx': 66, 'dblbk': 34, 'fglaq': 14}


def func3():
    return 18


def func4():
    return [48, 78, 22]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
