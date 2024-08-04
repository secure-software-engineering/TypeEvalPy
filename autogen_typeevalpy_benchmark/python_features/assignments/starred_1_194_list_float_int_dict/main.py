# Functions are assigned to variables via starred assignment
def func1():
    return [89, 18, 17]


def func2():
    return 37.23


def func3():
    return 77


def func4():
    return {'dakpb': 15, 'tsgvz': 97, 'xrdgy': 59}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
