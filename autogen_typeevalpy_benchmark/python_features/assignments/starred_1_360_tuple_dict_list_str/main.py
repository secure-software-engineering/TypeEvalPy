# Functions are assigned to variables via starred assignment
def func1():
    return (99, 4, 22)


def func2():
    return {'pumua': 50, 'zwbwv': 96, 'wcoxo': 84}


def func3():
    return [12, 77, 38]


def func4():
    return 'pudxq'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
