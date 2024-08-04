# Functions are assigned to variables via starred assignment
def func1():
    return 'ezrdf'


def func2():
    return {'vqcpl': 4, 'ylhcu': 10, 'hmcjd': 34}


def func3():
    return 66.53


def func4():
    return 32

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
