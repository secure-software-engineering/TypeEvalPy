# Functions are assigned to variables via starred assignment
def func1():
    return 'srcnr'


def func2():
    return 70.31


def func3():
    return {'gifkv': 79, 'cqndg': 23, 'kpdvo': 84}


def func4():
    return 90

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
