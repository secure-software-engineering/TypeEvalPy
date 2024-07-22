# Functions are assigned to variables via starred assignment
def func1():
    return 45


def func2():
    return 52.81


def func3():
    return {'hdbcf': 88, 'egimu': 45, 'bcihp': 55}


def func4():
    return 'behzn'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
