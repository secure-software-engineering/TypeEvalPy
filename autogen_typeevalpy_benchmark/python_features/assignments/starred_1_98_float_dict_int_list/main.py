# Functions are assigned to variables via starred assignment
def func1():
    return 93.97


def func2():
    return {'jilyl': 96, 'cixvz': 13, 'pxcpa': 27}


def func3():
    return 83


def func4():
    return [49, 54, 37]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
