# Functions are assigned to variables via starred assignment
def func1():
    return 47


def func2():
    return {'pumgc': 63, 'nktbv': 72, 'pzuia': 15}


def func3():
    return 45.68


def func4():
    return [10, 81, 44]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
