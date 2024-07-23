# Functions are assigned to variables via starred assignment
def func1():
    return 'fxsjy'


def func2():
    return (88, 65, 50)


def func3():
    return [85, 12, 58]


def func4():
    return {'mohne': 11, 'pxjwi': 98, 'khabr': 76}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
