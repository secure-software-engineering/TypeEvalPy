# Functions are assigned to variables via starred assignment
def func1():
    return 35


def func2():
    return [53, 90, 75]


def func3():
    return 74.65


def func4():
    return {'zaddq': 23, 'eusym': 78, 'kynqm': 19}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
