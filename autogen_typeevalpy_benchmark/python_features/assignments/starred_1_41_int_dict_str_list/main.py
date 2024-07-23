# Functions are assigned to variables via starred assignment
def func1():
    return 48


def func2():
    return {'fggur': 56, 'xrkal': 29, 'icnsr': 61}


def func3():
    return 'uubct'


def func4():
    return [76, 3, 32]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
