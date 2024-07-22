# Functions are assigned to variables via starred assignment
def func1():
    return 85.98


def func2():
    return 6


def func3():
    return 'sxyus'


def func4():
    return {'puiff': 74, 'uwtle': 94, 'ecffx': 93}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
