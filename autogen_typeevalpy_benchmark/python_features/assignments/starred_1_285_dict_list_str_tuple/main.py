# Functions are assigned to variables via starred assignment
def func1():
    return {'cfjsn': 39, 'gteln': 59, 'gsdpm': 56}


def func2():
    return [64, 51, 39]


def func3():
    return 'iirkr'


def func4():
    return (49, 74, 100)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
