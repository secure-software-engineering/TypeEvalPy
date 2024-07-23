# Functions are assigned to variables via starred assignment
def func1():
    return (91, 78, 17)


def func2():
    return {'vlzzf': 94, 'sqnmy': 20, 'lluhj': 55}


def func3():
    return 55.31


def func4():
    return 2

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
