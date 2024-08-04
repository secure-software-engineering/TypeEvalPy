# Functions are assigned to variables via starred assignment
def func1():
    return 73.24


def func2():
    return {'qrnll': 75, 'oplkc': 7, 'swaww': 11}


def func3():
    return 34


def func4():
    return 'qxczf'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
