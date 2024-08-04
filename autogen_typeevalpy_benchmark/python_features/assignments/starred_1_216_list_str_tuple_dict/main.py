# Functions are assigned to variables via starred assignment
def func1():
    return [62, 14, 76]


def func2():
    return 'uvchm'


def func3():
    return (20, 2, 14)


def func4():
    return {'drdjv': 71, 'iabip': 27, 'azsrp': 73}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
