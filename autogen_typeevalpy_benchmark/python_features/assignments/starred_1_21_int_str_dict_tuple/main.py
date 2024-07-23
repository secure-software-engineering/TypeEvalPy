# Functions are assigned to variables via starred assignment
def func1():
    return 95


def func2():
    return 'zjvda'


def func3():
    return {'wywfx': 82, 'fuozm': 62, 'dpydp': 22}


def func4():
    return (79, 49, 15)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
