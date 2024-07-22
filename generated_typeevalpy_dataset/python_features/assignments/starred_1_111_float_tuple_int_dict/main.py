# Functions are assigned to variables via starred assignment
def func1():
    return 49.37


def func2():
    return (55, 59, 82)


def func3():
    return 2


def func4():
    return {'pzhlm': 22, 'iovid': 79, 'fifuv': 7}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
