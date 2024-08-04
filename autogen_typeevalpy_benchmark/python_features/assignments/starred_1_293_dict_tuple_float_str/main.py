# Functions are assigned to variables via starred assignment
def func1():
    return {'gfnsm': 3, 'bdmtr': 40, 'dovvx': 91}


def func2():
    return (21, 33, 6)


def func3():
    return 76.57


def func4():
    return 'ziixn'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
