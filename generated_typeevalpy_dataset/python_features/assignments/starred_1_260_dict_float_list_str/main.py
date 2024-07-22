# Functions are assigned to variables via starred assignment
def func1():
    return {'ppnli': 35, 'gajje': 59, 'xpkmz': 27}


def func2():
    return 64.58


def func3():
    return [46, 11, 95]


def func4():
    return 'ipbov'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
