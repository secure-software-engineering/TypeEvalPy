# Functions are assigned to variables via starred assignment
def func1():
    return {'pyymo': 19, 'gmueg': 80, 'ceibh': 24}


def func2():
    return [55, 58, 55]


def func3():
    return 'qnqlz'


def func4():
    return 52.95

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
