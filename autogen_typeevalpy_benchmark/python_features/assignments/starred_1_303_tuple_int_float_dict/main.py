# Functions are assigned to variables via starred assignment
def func1():
    return (5, 47, 92)


def func2():
    return 85


def func3():
    return 17.31


def func4():
    return {'miosh': 77, 'vpgdx': 12, 'gehao': 15}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
