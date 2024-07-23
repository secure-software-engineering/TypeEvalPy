# Functions are assigned to variables via starred assignment
def func1():
    return {'qsnpx': 100, 'mtxmx': 97, 'kfynb': 84}


def func2():
    return 'kleke'


def func3():
    return [66, 95, 20]


def func4():
    return 24.94

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
