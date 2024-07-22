# Functions are assigned to variables via starred assignment
def func1():
    return {'mbtcz': 50, 'mipzj': 93, 'npewb': 4}


def func2():
    return (25, 63, 18)


def func3():
    return 92


def func4():
    return [97, 53, 70]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
