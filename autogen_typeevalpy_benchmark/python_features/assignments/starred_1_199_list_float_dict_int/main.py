# Functions are assigned to variables via starred assignment
def func1():
    return [56, 39, 59]


def func2():
    return 41.25


def func3():
    return {'wqhlm': 19, 'vsirb': 93, 'xegkm': 91}


def func4():
    return 96

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
